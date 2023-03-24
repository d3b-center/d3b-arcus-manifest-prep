from arcus_manifests.common.constants import ALL_GENERATOR_LIST
from arcus_manifests.generator.file.build_manifest import build_file_table

import pandas as pd
from d3b_cavatica_tools.utils.logging import get_logger

# from arcus_manifests.generator.participant.build_manifest import (
#     build_participant_table,
# )
# from arcus_manifests.generator.participant_crosswalk.build_manifest import (
#     build_participant_crosswalk_table,
# )


logger = get_logger(__name__, testing_mode=False)


def generate_submission_package(
    postgres_connection_url, submission_package_dir, seed_file, generator_list
):
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
    # participant_list = (
    #     file_sample_participant_map["participant_id"]
    #     .drop_duplicates()
    #     .to_list()
    # )
    # sample_list = (
    #     file_sample_participant_map["sample_id"].drop_duplicates().to_list()
    # )
    file_list = (
        file_sample_participant_map["file_id"].drop_duplicates().to_list()
    )
    # Save the seed file
    file_sample_participant_map.to_csv(
        f"{submission_package_dir}/file_sample_participant_map.csv", index=False
    )

    if "file" in generator_list:
        build_file_table(
            postgres_connection_url, file_list, submission_package_dir
        )
