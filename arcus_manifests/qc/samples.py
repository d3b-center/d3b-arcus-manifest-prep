from arcus_manifests.qc.report import report_qc_result

from d3b_cavatica_tools.utils.logging import get_logger
from tqdm import tqdm

logger = get_logger(__name__, testing_mode=False)


def qc_samples(
    sample_list_fsp,
    sample_list_participant_manifest,
    sample_list_file_manifest,
):
    """QC Relations between samples

    Test that, for every item in all input lists, each item is in all lists.

    :param sample_list_fsp: list of samples in the sample manifest
    :type sample_list_fsp: list
    :param sample_list_participant_manifest: list of samples in the file-sample-participant
    mapping
    :type sample_list_participant_manifest: list
    :param sample_list_file_manifest: list of samples in the genomic_info
    manifest
    :type sample_list_file_manifest: list
    :return: Information about item membership in each input list. Dict of dicts
    where each key is an identifier and the value is a dict describing if the
    item is in each input list.
    :rtype: dict
    """
    all_samples = list(
        set(
            sample_list_fsp
            + sample_list_participant_manifest
            + sample_list_file_manifest
        )
    )
    result_dict = {
        i: {
            "in_fsp": None,
            "in_participant_manifest": None,
            "in_file_manifest": None,
        }
        for i in all_samples
    }
    logger.info("Checking that all samples are in all manifests")
    not_in_fsp = []
    not_in_participant_manifest = []
    not_in_file_manifest = []
    for sample in tqdm(all_samples):
        in_fsp = sample in sample_list_fsp
        in_participant_manifest = sample in sample_list_participant_manifest
        in_file_manifest = sample in sample_list_file_manifest
        result_dict[sample]["in_fsp"] = in_fsp
        result_dict[sample]["in_participant_manifest"] = in_participant_manifest
        result_dict[sample]["in_file_manifest"] = in_file_manifest
        if not in_fsp:
            not_in_fsp.append(sample)
            logger.debug(f"{sample} not in fsp")
        if not in_participant_manifest:
            not_in_participant_manifest.append(sample)
            logger.debug(f"{sample} not in participant manifest")
        if not in_file_manifest:
            not_in_file_manifest.append(sample)
            logger.debug(f"{sample} not in file manifest")
    report_qc_result(len(not_in_fsp), "samples", "fsp")
    report_qc_result(
        len(not_in_participant_manifest), "samples", "participant_manifest"
    )
    report_qc_result(len(not_in_file_manifest), "samples", "file manifest")
    return result_dict
