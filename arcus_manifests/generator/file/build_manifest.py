from arcus_manifests.common.queries import file_query
from arcus_manifests.common.standard import order_columns

import pandas as pd
import psycopg2
from d3b_cavatica_tools.utils.logging import get_logger

logger = get_logger(__name__, testing_mode=False)


def build_file_table(db_url, file_list, submission_package_dir):
    """Build the file table

    Build the file manifest

    :param db_url: database url
    :type db_url: str
    :param file_list: file IDs to have in the file manifest
    :type file_list: list
    :param submission_package_dir: directory to save the output manifest
    :type submission_package_dir: str
    :return: file table
    :rtype: pandas.DataFrame
    """
    logger.info("Building file table")
    column_order = [
        "biosample_id",
        "file_type",
        "protocol",
        "file_path",
        "file_groups",
    ]
    logger.info("connecting to database")
    conn = psycopg2.connect(db_url)

    logger.info("Querying for manifest of files")
    file_table = pd.read_sql(file_query(file_list), conn)
    # Set the column order and sort on key column
    file_table = order_columns(file_table, column_order).sort_values("file_id")
    logger.info("saving file manifest to file")
    file_table.to_csv(f"{submission_package_dir}/file.csv", index=False)
    return file_table
