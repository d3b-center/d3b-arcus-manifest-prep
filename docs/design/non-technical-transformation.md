# Overview

The ARCUS Manifests are seeded with a file that maps files to samples and
participants, the `file-sample-participant mapping` (`FSP mapping`). The FSP
mapping is then used to generate all of the required manifests

## File-Sample-Participant (FSP) Mapping

The FSP mapping maps files, samples, and participants to one another. The FSP
has the following columns:

- `participant_id`: the Kids First ID for the participant, e.g. `PT_ABCD1234`.
- `sample_id`: the Kids First ID for the sample, e.g. `BS_ABCD1234`.
- `genomic_file_id`: the Kids First ID for the gile, e.g. `GF_ABCD1234`.
- `research_id`: the C-ID of the participant, e.g. `C123456`.
- `sdg_id`: the SDG ID or "7316 number" of the sample, e.g. `7316-1`.
- `aliquot_id`: the aliquot's ID. The format of this identifier varies.
- `file_name`: the filename of the file in question, e.g. `my_file.cram`.

The FSP mapping has one line for each mapping of `participant_id` to `sample_id`
to `genomic_file_id`.

This file is the master list of all files, participants, and samples that are in
any of the manifests.

## Derived Manifests

Each section below has the description of the manifest from the ARCUS readme,
the data dictionary supplied by ARCUS, and general, non-technical instructions
for how each column in the manifest is derived.

The output manifests that we produce are expected to follow the exact same
column order as the data dictionary. Likewise, each manifest should be ordered
by the specified column.

### Participant Crosswalk

> participant-crosswalk.txt is a tab delimited file with no header that links
> `local_participant_id` in PARTICIPANT_MANIFEST to MRNs.

The sample manifest can be found [here](../../rdm-project-template/manifests/participant-crosswalk.txt).

#### Participant Crosswalk Data Dictionary

<!-- markdownlint-disable -->
| **column**               | **definition**                                 | **type** | **notes**                                                      |
|--------------------------|------------------------------------------------|----------|----------------------------------------------------------------|
| **local_id_type**        | The type of participant ID (local).            | String   | This will always be local.                                     |
| **local_participant_id** | ID that is used in PARTICIPANT_MANIFEST        | String   |                                                                |
| **auth_id_type**         | The type of participant id(chop)               | String   | This will always be chop.                                      |
| **auth_participant_id**  | Authorative ID of the participant. (Often MRN) | String   | Use an 8 digit MRN. Left-pad the MRN with zeroes as necessary. |
<!-- markdownlint-enable -->

#### Participant Crosswalk Construction

From the FSP mapping, extract the following columns and take the unique rows:

- `research_id`

Map each research ID to MRNs in the MRN c-id mapping table.

Rename the `research_id` to be `local_participant_id`. Rename the column with
MRNs to be `auth_participant_id`. Set the value of `local_id_type` to be
`local`. Set the value of `auth_id_type` to be `chop`.

### Participant Manifest

> participant_manifest.csv matches participants/patients to cohorts and
> biosample IDs. Ideally, biosample_id links to the CHOP biobank. When you
> cannot link the the biobank, treat biosample_id as the IDs you use for samples
> taken from participants. If you deal with only one sample type, you might use
> the participant ID. If you run a treatment/control experiment, you might use
> {participantID}_treat and {participantID}_control as as a biosample ID scheme.
> If you work with different tissue samples from participants, you might use
> {participantID}_{tissue} as a biosample ID scheme. See participant data
> dictionary for definitions of each column.

The sample manifest can be found [here](../../rdm-project-template/manifests/participant_manifest.csv).

#### Participant Manifest Data Dictionary
<!-- markdownlint-disable -->
| **column**               | **definition**                                                                                                                | **type** |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------|
| **local_participant_id** | This ID uniquely defined a person, and can be linked to an MRN.                                                               | String   |
| **cohort**               | Use this column to group participants into cohorts that will be cwmpared (For example, case vs healthy control).              | String   |
| **biosample_id**         | Ideally, this ID can link to the CHOP biobank. When this is not possible, use the sample ID from your project.                | String   |
<!-- markdownlint-enable -->

#### Participant Manifest Construction

From the FSP mapping, extract the following columns and take the unique rows:

- `research_id`
- `aliquot_id`

The `research_id` column will be renamed to be the `local_participant_id`. The
`aliquot_id` column will be renamed to be the `biosample_id`. These extracted
columns will form the first part of the participant_manifest.

The value in the cohort column will be `CBTN`.

From the FSP mapping, take the list of unique `participant_id`s and query from
the Kids First schema in the D3B Warehouse, the associated `family_id`. This
family ID is the Kids First ID of the participant's family. join these derived
family_ids to the columns extracted above

All participants submitted to ARCUS are expected to be CHOP patients, so we
should expect that each participant is a proband. Confirm this with the
following procedure:

From the FSP mapping, take the list of unique `participant_id`s and query from
the Kids First schema in the D3B Warehouse, the value `is_proband`.

If it is true that every participant we are submitting to ARCUS is a proband,
the value of this column should be "proband".

### File Manifest

> file_manifest.csv matches biosample IDs to data files and experimental
> protocols, described in yaml files. Many files might share the same
> experimental protocol. These yaml protocol files describe experiment and data
> processing details.

The sample manifest can be found [here](../../rdm-project-template/manifests/file_manifest.csv).

#### File Manifest Data Dictionary

<!-- markdownlint-disable -->
| **column** | **definition** | **type** |
|---|---|---|
| **biosample_id** | This ID links to PARTICIPANT_MANIFEST. | String |
| **file_type** | Each experiment template has a list of required file types. Use those terms. | String |
| **Each experiment template has protocol yaml files or capture kit information used to describe experiment metadata. This column points to the file path of the protocol or the capture kit information for this file. Paths should start with references/procotols/ or data/ref-data/platform-data** | String |  |
| **file_path** | Use one file path per row. It should start with data/. | String |
| **file_groups** | Files in the same group are related. Paired fastq files belong in the same group. A bam file and its index belong in the same group. Plink bfiles belong in the same group. | String |
| **derived_from_file_group** | "This column describes relations between file groups. We want to capture consecutive pipeline steps. For example, a bam file is derived from a paired fastq group. Use the name of the file_groups used to construct this file. Delimit multiple groups with a semicolon. Use NA when there are no prior step files to reference." | String |
<!-- markdownlint-enable -->

#### File Manifest Construction

From the FSP mapping, extract the following columns and take the unique columns:

- `aliquot_id`
- `file_name`

To compute the value for `file_type`, extract the file format value from the
`file_name`. This should be either `cram` or `crai`.

To compute the value for `file_groups`, extract the UUID from the `file_name`.
Extract this value because crams and their associate index files share the same
UUID in the filename but with different extensions.

To compute the value for `file_path`, prepend each `file_name` with
`data/kf-study-us-east-1-prd-sd-bhjxbdqk/harmonized/cram/`

### File Derivations

> file_derivation.csv describes the relationships between files in a pipeline or
> workflow

The sample manifest can be found [here](../../rdm-project-template/manifests/file_derivation.csv)

We are not generating a file derivations manifest because none of the files we
submitted to arcus are derived from any other files we submitted. All the files
we submitted are only workflow output crams and their associated index files.

### Environment Manifest

> env_manifest.csvEnvironment files are necessary for all scripts and machine
> models, and document the environment in which it was created and run. The
> environment_manifest.csv links the script or machine model and the environment
> file stored within the configs directory.

The sample manifest can be found [here](../../rdm-project-template/manifests/env_manifest.csv)

We are not generating an environment manifest because we did not submit any
scripts or machine models.
