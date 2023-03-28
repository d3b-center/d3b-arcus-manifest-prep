"""
Copies contents of prd dataservice to local dataservice for a particular study
"""
from arcus_manifests.common.constants import (
    ALL_GENERATOR_LIST,
    DB_URL_DEFAULT,
    FSP_DEFAULT,
    SUBMISSION_PACKAGE_DIR_DEFAULT,
)
from arcus_manifests.generator.generate import generate_submission_package
from arcus_manifests.qc.qc import qc_submission_package

import click
import pkg_resources


@click.group()
@click.version_option(package_name="d3b-arcus-manifest-tools")
@click.option(
    "-c",
    "--postgres_connection_url",
    type=str,
    required=True,
    default=DB_URL_DEFAULT,
    help="Connection URL to KF Postgres",
)
@click.option(
    "-d",
    "--submission_packager_dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
    required=False,
    default=SUBMISSION_PACKAGE_DIR_DEFAULT,
    show_default=True,
    help="Location of directory that has the submission package.",
)
@click.pass_context
def arcus_manifests(ctx, postgres_connection_url, submission_packager_dir):
    """
    Tools related to handling ARCUS manifest generation and QC.

    Our submission package to ARCUS has three documents. See the
    non technical overview for more information about the elements
    in each file:

    \b
    1. participant_crosswalk.csv
    2. participant.csv
    3. file_manifest.csv
    \f

    Non Technical Overview Link: https://github.com/d3b-center/d3b-arcus-manifest-prep/blob/main/docs/design/non-technical-transformation.md

    :param ctx: context to allow different commands to interact with each other
    :type ctx: click.Context
    :param postgres_connection_url: postgres connection url. takes the form
    postgresql://[user]:[password]@[host]:[port]/[database_name]
    :type postgres_connection_url: str
    :param submission_packager_dir: Directory of submission package. Ends in
    trailing backslash, e.g. `path/to/dir/`
    :type submission_packager_dir: str
    """  # noqa
    ctx.ensure_object(dict)
    ctx.obj["postgres_connection_url"] = postgres_connection_url
    ctx.obj["submission_packager_dir"] = submission_packager_dir
    pass


@arcus_manifests.command("generate")
@click.option(
    "-f",
    "--seed_file",
    type=click.Path(exists=True, dir_okay=False),
    required=True,
    default=pkg_resources.resource_filename("arcus_manifests", FSP_DEFAULT),
    help="CSV file that maps all the files, samples, and participants to "
    + "use to generate the manifests.",
)
@click.option(
    "-m",
    "--mrn_map_file",
    type=click.Path(exists=True, dir_okay=False),
    required=True,
    help="CSV file that maps research IDs (C-IDs) to MRNs.",
)
@click.option(
    "-u",
    "--allow_unvalidated_mrn",
    is_flag=True,
    default=False,
    show_default=True,
    type=click.Path(exists=True, dir_okay=False),
    help="Flag. Should MRNs that do not pass validation be allowed. "
    "If True, when an mrn fails validation, a warning is shown and execution "
    "continues. By default, when MRNs fail validation, execution is halted.",
)
@click.option(
    "-g",
    "--table_to_generate",
    "generator",
    multiple=True,
    type=click.Choice(
        ALL_GENERATOR_LIST,
        case_sensitive=False,
    ),
    default=["all"],
    show_default=True,
)
@click.pass_context
def generate_submission(
    ctx, seed_file, mrn_map_file, allow_unvalidated_mrn, generator
):
    """
    Generate an ARCUS submission manifest or manifests using a seed
    file_sample_participant mapping.
    """
    generate_submission_package(
        ctx.obj["postgres_connection_url"],
        ctx.obj["submission_packager_dir"],
        seed_file,
        mrn_map_file,
        allow_unvalidated_mrn,
        generator,
    )


@arcus_manifests.command("qc")
@click.pass_context
def qc_submission(ctx):
    """QC an ARCUS Submission Package"""
    qc_submission_package(
        # ctx.obj["postgres_connection_url"], ctx.obj["submission_packager_dir"]
    )


if __name__ == "__main__":
    arcus_manifests()  # pylint: disable=no-value-for-parameter
