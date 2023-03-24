def order_columns(manifest, columns):
    """order columns in the manifest

    :param manifest: The manifest to order columns for
    :type manifest: pandas.DataFrame
    :param columns: The columns in the manifest ordered correctly
    :type columns: list
    :return: The manifest with columns needed in the correct order
    :rtype: pandas.DataFrame
    """
    columns = [
        "file_id",
        "file_name",
        "file_type",
        "file_size",
        "md5sum",
        "file_url_in_cds",
        "controlled_access",
    ]
    return manifest[columns]
