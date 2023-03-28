from arcus_manifests.common.standard import order_columns

from d3b_cavatica_tools.utils.logging import get_logger

logger = get_logger(__name__, testing_mode=False)


def validate_mrn(mrn):
    """Validate MRNs

    Validates that the MRN can be coerced to be integer and that the mrn is no
    greater than 8 characters long, Returned MRN is zero-padded to be 8
    characters long

    :param mrn: an MRN
    :type mrn: str or int
    :return: zero-padded, 8 character-long MRN
    :rtype: str
    """
    if not (isinstance(mrn, int) or mrn.isdigit()):
        raise ValueError("MRN must be coercible to integer")
    if len(str(mrn)) > 8:
        raise ValueError("MRNs cannot be longer than 8 characters")
    return f"{int(mrn):08}"


def build_participant_crosswalk_table(
    participant_list, mrn_map, submission_package_dir
):
    logger.info("Building Participant Crosswalk Table")
    column_order = [
        "local_id_type",
        "local_participant_id",
        "auth_id_type",
        "auth_participant_id",
    ]
    participant_mrn_map = mrn_map[mrn_map["research_id"].isin(participant_list)]
    participant_mrn_map["mrn"] = participant_mrn_map["mrn"].apply(validate_mrn)
    participant_mrn_map = participant_mrn_map.rename(
        columns={
            "research_id": "local_participant_id",
            "mrn": "auth_participant_id",
        }
    )
    participant_mrn_map["local_id_type"] = "local"
    participant_mrn_map["auth_id_type"] = "chop"
    crosswalk_table = order_columns(
        participant_mrn_map, column_order
    ).sort_values("local_participant_id")
    logger.info("Saving participant_crosswalk to file")
    crosswalk_table.to_csv(
        f"{submission_package_dir}/participant-crosswalk.txt",
        sep="\t",
        header=False,
        index=False,
    )
    return crosswalk_table
