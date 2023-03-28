from arcus_manifests.common.standard import order_columns

from d3b_cavatica_tools.utils.logging import get_logger

logger = get_logger(__name__, testing_mode=False)


def build_participant_table(
    file_sample_participant_map, submission_package_dir
):
    """Build the Participant table

    :param file_sample_participant_map: table mapping files to samples and
    participants
    :type file_sample_participant_map: pandas.DataFrame
    :param submission_package_dir: directory to save the output manifest
    :type submission_package_dir: str
    :return: participant table
    :rtype: pandas.DataFrame
    """
    logger.info("Building Participant Table")
    column_order = ["local_participant_id", "cohort", "biosample_id"]
    file_sample_participant_map["cohort"] = "CBTN"
    participant_table = file_sample_participant_map[column_order]
    participant_table = order_columns(
        participant_table, column_order
    ).sort_values(["local_participant_id", "biosample_id"])
    logger.info("Saving participant table to file")
    participant_table.to_csv(
        f"{submission_package_dir}/participant_manifest.csv", index=False
    )
    return participant_table
