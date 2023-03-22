# ARCUS Manifest Seed Files

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

This file was generated with the sql script [here](../../scripts/arcus-file-sample-participant-map.sql).