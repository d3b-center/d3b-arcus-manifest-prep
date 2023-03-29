from arcus_manifests.qc.files import qc_files
from arcus_manifests.qc.participants import qc_participants
from arcus_manifests.qc.samples import qc_samples

import pandas as pd
from d3b_cavatica_tools.utils.logging import get_logger

logger = get_logger(__name__, testing_mode=False)


def qc_submission_package(submission_packager_dir):
    """QC A submission Package

    :param submission_packager_dir: directory to load the manifests from
    :type submission_packager_dir: str
    """
    logger.info(f"Loading manifests in {submission_packager_dir}")
    # Load the individual manifests
    fsp = pd.read_csv(
        submission_packager_dir + "file_sample_participant_map.csv"
    )
    file_manifest = pd.read_csv(submission_packager_dir + "file_manifest.csv")
    participant_manifest = pd.read_csv(
        submission_packager_dir + "participant_manifest.csv"
    )
    participant_crosswalk = pd.read_csv(
        submission_packager_dir + "participant-crosswalk.txt",
        sep="\t",
        header=None,
    )
    # generate lists
    logger.info("generating unique lists of items from manifests")
    participant_list_fsp = fsp["research_id"].drop_duplicates().to_list()
    participant_list_participant_manifest = (
        participant_manifest["local_participant_id"].drop_duplicates().to_list()
    )
    participant_list_crosswalk = (
        participant_crosswalk[1].drop_duplicates().to_list()
    )
    sample_list_fsp = fsp["aliquot_id"].drop_duplicates().to_list()
    sample_list_participant_manifest = (
        participant_manifest["biosample_id"].drop_duplicates().to_list()
    )
    sample_list_file_manifest = (
        file_manifest["biosample_id"].drop_duplicates().to_list()
    )
    file_list_fsp = fsp["file_name"].drop_duplicates().to_list()
    file_list_file_manifest = (
        file_manifest["file_path"]
        .apply(lambda x: x.rpartition("/")[2])
        .drop_duplicates()
        .to_list()
    )

    # run QC
    participant_qc_dict = qc_participants(
        participant_list_fsp,
        participant_list_participant_manifest,
        participant_list_crosswalk,
    )
    sample_qc_dict = qc_samples(
        sample_list_fsp,
        sample_list_participant_manifest,
        sample_list_file_manifest,
    )
    file_qc_dict = qc_files(
        file_list_fsp,
        file_list_file_manifest,
    )
    pd.DataFrame.from_dict(participant_qc_dict, orient="index").to_csv(
        "qc-participant.csv"
    )
    pd.DataFrame.from_dict(sample_qc_dict, orient="index").to_csv(
        "qc-samples.csv"
    )
    pd.DataFrame.from_dict(file_qc_dict, orient="index").to_csv("qc-files.csv")
