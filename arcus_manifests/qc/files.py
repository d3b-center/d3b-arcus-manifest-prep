from arcus_manifests.qc.report import report_qc_result

from d3b_cavatica_tools.utils.logging import get_logger
from tqdm import tqdm

logger = get_logger(__name__, testing_mode=False)


def qc_files(file_list_fsp, file_list_file_manifest):
    """QC Relations between files

    Test that, for every item in all input lists, each item is in all lists.

    :param file_list_fsp: list of files in the file-sample-participant mapping
    :type file_list_fsp: list
    :param file_list_file_manifest: list of files in the file manifest
    :type file_list_file_manifest: list
    :return: Information about item membership in each input list. Dict of dicts
    where each key is an identifier and the value is a dict describing if the
    item is in each input list.
    :rtype: dict
    """
    all_files = list(set(file_list_fsp + file_list_file_manifest))
    result_dict = {
        i: {
            "in_fsp": None,
            "in_file_manifest": None,
        }
        for i in all_files
    }
    logger.info("Checking that all files are in all manifests")
    not_in_fsp = []
    not_in_file_manifest = []
    for file in tqdm(all_files):
        in_fsp = file in file_list_fsp
        in_file_manifest = file in file_list_file_manifest
        result_dict[file]["in_fsp"] = in_fsp
        result_dict[file]["in_file_manifest"] = in_file_manifest
        if not in_fsp:
            not_in_fsp.append(file)
            logger.debug(f"{file} not in fsp")
        if not in_file_manifest:
            not_in_file_manifest.append(file)
            logger.debug(f"{file} not in file_manifest")
    report_qc_result(len(not_in_fsp), "files", "fsp")
    report_qc_result(len(not_in_file_manifest), "files", "file_manifest")
    return result_dict
