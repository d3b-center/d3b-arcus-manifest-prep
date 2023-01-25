## `data/`

### Summary
The goal of `data/` is to maintain descriptions of authoritative source data and their associated files and metadata in both raw and processed formats. Use the `manifests` directory to store metadata for these files. See [project-metadata](https://github.research.chop.edu/arcus/arcus-ingestion) for a description of manifests and metadata.

#### Organization:
* `data/raw/` - holds lab or CHOP center generated data that should never be deleted. Raw patient files should be listed in FILE_MANIFEST.
* `data/interim/` - an unregulated space to put intermediate and temporary files
* `data/ref-data/` - external/public datasets that are not supplied by RIS or your lab. Follow [RIS reference_data structure](https://github.research.chop.edu/RIS/reference_data).
* `data/endpoints/` - generated files to support papers or grants. Try to organize file by type endpoint subdirectories by file type (bam, fastq, etc). Patient endpoint files should be listed in [`manifests/file_manifest.csv`]([manifests/file_manifest.csv](https://github.research.chop.edu/CRU/Minds-Matter-Concussion-Care/blob/main/manifests/file_manifest.csv)).

## Admin Notes

This sub-directory is required. For Arcus Labs this sub-directory is maintained and managed jointly by Arcus and the research study team.

