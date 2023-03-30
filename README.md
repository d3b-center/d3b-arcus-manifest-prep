# D3b Arcus-CBTN transfer manifest prep
<!-- markdownlint-disable -->
<p align="center">
  <a href="https://github.com/d3b-center/d3b-arcus-manifest-prep/blob/master/LICENSE"><img src="https://img.shields.io/github/license/d3b-center/d3b-arcus-manifest-prep"></a>
  <a href="https://github.com/marketplace/actions/super-linter"><img src="https://github.com/d3b-center/d3b-arcus-manifest-prep/workflows/Lint%20Code%20Base/badge.svg"></a>
  <a href="https://gitmoji.dev"><img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square" alt="Gitmoji"/></a>
  <a href="https://github.com/d3b-center/d3b-arcus-manifest-prep/releases/tag/0.1.0"><img src="https://img.shields.io/github/v/release/d3b-center/d3b-arcus-manifest-prep"></a>
</p>
<!-- markdownlint-restore -->

Tool to generate manifests for ARCUS for the CBTN CHOP patient data transfer.

See the [Design Overview](docs/design_overview.md) for a discussion on how the
manifests are created and how to use the tool to generate manifests.

## Installation

Recommend installation procedure is to install the manifest generator with
[`pipx`](https://pypa.github.io/pipx). `pipx` can be installed on macOS with
`brew` and on Linux and Windows with `pip`. `pipx` is recommended over other
methods because it installs the CLI in its own virtual environment and then puts
the CLI on your machine's PATH. Please follow the instructions for installing
`pipx` [here](https://pypa.github.io/pipx/installation/).

### Install latest release

After installing `pipx`, to install the manifest generator, run:

```sh
pipx install git+https://github.com/d3b-center/d3b-arcus-manifest-prep@latest-release
```

### Install Most Recent Development Version

```python
pipx install git+https://github.com/d3b-center/d3b-arcus-manifest-prep.git
```

## Using the Tool

### Building Manifests

To build manifests, specify the database connection URL to the Kidsfirst
Database and the research_id-mrn mapping file's location:

```sh
arcus_manifests -c $DATABASE_URL  generate -m  ~/mount/stg_cbtn_enrollment.csv -u
```

### QC

To QC a submission manifest, pass the tool the URL to the D3B Warehouse. This
connection is used to make sure that participants are only ones expected to be
in the manifests.

<!-- markdownlint-disable -->
```sh
arcus_manifests -c $D3BWAREHOUSE_URL -d  ~/Downloads/submission_packet_v0.1.0/manifests/ qc
```
<!-- markdownlint-restore -->

## Developer Notes

### Releases

This repository is setup to take advantage of the [d3b-release-maker](https://github.com/d3b-center/d3b-release-maker/).
Please follow the instructions there to build releases.

### Linting

This repository is setup to take advantage of the [GitHub Super Linter](https://github.com/marketplace/actions/super-linter).
Of note are the markdownlint files and the pyproject.toml.
