# How to generate a new version of the ARCUS Manifests

## Setup

n.b. the below is currently a *plan* for how the manifests will be generated, to
be updated and refined as code is written.

### Installation

Recommend installation procedure is to install the manifest generator with
[`pipx`](https://pypa.github.io/pipx). `pipx` can be installed on macOS with
`brew` and on Linux and Windows with `pip`. `pipx` is recommended over other
methods because it installs the CLI in its own virtual environment and then puts
the CLI on your machine's PATH. Please follow the instructions for installing
`pipx` [here](https://pypa.github.io/pipx/installation/).

After installing `pipx`, to install the manifest generator, run:

```sh
pipx install git+https://github.com/d3b-center/d3b-arcus-manifest-prep@latest-release
```

### Database Credentials

Once the manifest generator is installed, the next step is to make sure that you
have access to the d3b warehouse and that your connection credentials are
available to you.

### Data needed to build the manifests

There are two sets of data needed to build the manifests:

1. A file-sample-participant mapping. Information about this manifest can be
   found [here](non-technical-transformation.md#file-sample-participant-fsp-mapping)
2. A mapping of `research_id` (commonly the "C-ID" of a participant) to MRN.
   **Note that this document, because it has MRNs, contains PHI and must be
   treated confidentially**. This documented is expected to have a column named
   `research_id` and a column named `mrn`.

While the paths to these documents are able to be passed to the manifest
generator, by default, the manifest generator will use the copy of the
file-sample-participant mapping built into the library, [here](../../data/arcus-file-sample-participant-map.csv).

## Use

### Building Manifests

To build a new version of the manifests run the following:

```sh
arcus_manifests generate --fsp_path path/to/fsp.csv --mrn_map_path file/to/mrn_mapping.csv
```
