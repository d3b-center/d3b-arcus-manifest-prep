from arcus_manifests.common.constants import ALL_GENERATOR_LIST
from arcus_manifests.generator.file.build_manifest import build_file_table
from arcus_manifests.generator.participant.build_manifest import (
    build_participant_table,
)
from arcus_manifests.generator.participant_crosswalk.build_manifest import (
    build_participant_crosswalk_table,
)

import pandas as pd
from d3b_cavatica_tools.utils.logging import get_logger

logger = get_logger(__name__, testing_mode=False)


def generate_submission_package(
    postgres_connection_url,
    submission_package_dir,
    seed_file,
    mrn_map_file,
    allow_unvalidated_mrn,
    generator_list,
):
    """Generate a submission package

    Generate all the specified files in the arcus submission package.

    :param postgres_connection_url: database url
    :type postgres_connection_url: str
    :param submission_package_dir: directory to save the output manifest
    :type submission_package_dir: str
    :param seed_file: file mapping files to participants and samples
    :type seed_file: str
    :param mrn_map_file: file mapping research IDs to MRNs
    :type mrn_map_file: str
    :param allow_unvalidated_mrn: Should unvalidated MRNs be allowed?
    :type allow_unvalidated_mrn: boolean
    :param generator_list: manifests to generate
    :type generator_list: str or list
    """
    if "all" in generator_list:
        logger.info("Generating all manifests in submission packet")
        generator_list = ALL_GENERATOR_LIST
    else:
        logger.info(
            "Generating specified manifests in submission packet: "
            + str(generator_list)
        )

    logger.info("Reading seed file")
    file_sample_participant_map = pd.read_csv(seed_file)
    mrn_map = pd.read_csv(mrn_map_file)[["research_id", "mrn"]]
    participant_list = (
        file_sample_participant_map["research_id"].drop_duplicates().to_list()
    )
    file_list = (
        file_sample_participant_map["genomic_file_id"]
        .drop_duplicates()
        .to_list()
    )
    # Save the seed file
    file_sample_participant_map.to_csv(
        f"{submission_package_dir}/file_sample_participant_map.csv", index=False
    )
    if "participant_manifest" in generator_list:
        build_participant_table(
            file_sample_participant_map, submission_package_dir
        )
    if "participant_crosswalk" in generator_list:
        build_participant_crosswalk_table(
            participant_list,
            mrn_map,
            submission_package_dir,
            allow_unvalidated_mrn,
        )
    if "file_manifest" in generator_list:
        build_file_table(
            postgres_connection_url, file_list, submission_package_dir
        )
