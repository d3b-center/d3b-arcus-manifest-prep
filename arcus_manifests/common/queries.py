"""
SQL queries used to build manifests of things in the CCDI Genomics Bucket
"""


def file_query(file_list):
    """Build query for File Manifest

    Builds the query text for the file manifest. Sets the protocol to be the platform and instrument model
    (concatenated). The expectation is to point to separate yaml files that contain information related to
    preparing/sequencing/analyzing the data, but platform and instrument model are only a part of that. Since
    we don't have info related to yaml files in the dataservice, we will provide what we can. Otherwise it's
    acceptable to exclude this information altogether. See https://github.com/d3b-center/d3b-arcus-manifest-prep/
    blob/main/docs/design/non-technical-transformation.md#file-manifest for description of the file manifest output.

    :param file_list: List of files to include in the file manifest
    :type file_list: str
    :return: Text query to generate the file manifest
    :rtype: str
    """
    query = f"""
    SELECT external_aliquot_id biosample_id,
    file_format file_type,
    platform || ' ' || instrument_model protocol,
    'data/' || REPLACE(gf.external_id,'s3://','') file_path,
    split_part(split_part(gf.external_id,'cram/',2),'.',1) file_group,
    'NA' derived_from_file_group
    FROM biospecimen b
    JOIN biospecimen_genomic_file bgf
    ON bgf.biospecimen_id = b.kf_id
    JOIN genomic_file gf
    ON gf.kf_id = bgf.genomic_file_id
    LEFT JOIN sequencing_experiment_genomic_file segf
    ON segf.genomic_file_id = gf.kf_id
    LEFT JOIN sequencing_experiment se
    ON se.kf_id = segf.sequencing_experiment_id
    WHERE gf.kf_id in ({str(file_list)[1:-1]})
    """
    return query
