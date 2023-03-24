"""
SQL queries used to build manifests of things in the CCDI Genomics Bucket
"""


def file_query(file_list):
    query = f"""
    SELECT *
    FROM genomic_file
    WHERE kf_id in ({str(file_list)[1:-1]})
    """
    return query
