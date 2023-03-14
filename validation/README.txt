instructions for using validation binary:


Run chmod +x /path/to/binary.
Run command: ./template-validator --contrib=/path/to/contribution/repo
 
Notes:
The --contrib flag is required and is used to specify the top-level folder location of your data contribution. It is expected that the data contribution repo follows the project-template directory structure. The validator looks for the manifests/ subdirectory to validate the manifest files, and expects at least these three required files:
file_manifest.csv
participant_manifest.csv
participant-crosswalk.txt


This binary is no longer used internally by Arcus (they have switched to using Github Actions for validation) but the expectation is that it still runs effectively. Contact Nicole Feldman or the Arcus LS team with any questions or issues.