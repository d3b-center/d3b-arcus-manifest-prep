def order_columns(manifest, columns):
    """order columns in the manifest

    :param manifest: The manifest to order columns for
    :type manifest: pandas.DataFrame
    :param columns: The columns in the manifest ordered correctly
    :type columns: list
    :return: The manifest with columns needed in the correct order
    :rtype: pandas.DataFrame
    """
    return manifest[columns]
