from arcus_manifests.qc.report import report_qc_result

from d3b_cavatica_tools.utils.logging import get_logger
from tqdm import tqdm

logger = get_logger(__name__, testing_mode=False)


def qc_participants(
    participant_list_fsp,
    participant_list_participant_manifest,
    participant_list_crosswalk,
):
    """QC Relations between participants

    Test that, for every item in all input lists, each item is in all lists.

    :param participant_list_fsp: list of participants in the
    file-sample-participant mapping
    :type participant_list_fsp: list
    :param participant_list_participant_manifest: list of participants in the
    participant manifest
    :type participant_list_participant_manifest: list
    :param participant_list_crosswalk: list of participants in the participant
    crosswalk
    :type participant_list_crosswalk: list
    :return: Information about item membership in each input list. Dict of dicts
    where each key is an identifier and the value is a dict describing if the
    item is in each input list.
    :rtype: dict
    """
    all_participants = list(
        set(
            participant_list_fsp
            + participant_list_participant_manifest
            + participant_list_crosswalk
        )
    )
    result_dict = {
        i: {
            "in_fsp": None,
            "in_participant_manifest": None,
            "in_participant_crosswalk_manifest": None,
        }
        for i in all_participants
    }
    logger.info("Checking that all participants are in all manifests")
    not_in_fsp = []
    not_in_participant_manifest = []
    not_in_participant_crosswalk_manifest = []
    for participant in tqdm(all_participants):
        in_fsp = participant in participant_list_fsp
        in_participant_manifest = (
            participant in participant_list_participant_manifest
        )
        in_participant_crosswalk_manifest = (
            participant in participant_list_crosswalk
        )
        result_dict[participant]["in_fsp"] = in_fsp
        result_dict[participant][
            "in_participant_manifest"
        ] = in_participant_manifest
        result_dict[participant][
            "in_participant_crosswalk_manifest"
        ] = in_participant_crosswalk_manifest
        if not in_fsp:
            not_in_fsp.append(participant)
            logger.debug(f"{participant} not in fsp")
        if not in_participant_manifest:
            not_in_participant_manifest.append(participant)
            logger.debug(f"{participant} not in participant_manifest")
        if not in_participant_crosswalk_manifest:
            not_in_participant_crosswalk_manifest.append(participant)
            logger.debug(f"{participant} not in participant_crosswalk")
    report_qc_result(len(not_in_fsp), "participants", "fsp")
    report_qc_result(
        len(not_in_participant_manifest), "participants", "participant_manifest"
    )
    report_qc_result(
        len(not_in_participant_crosswalk_manifest),
        "participants",
        "participant_crosswalk",
    )
    return result_dict
