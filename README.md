# apiFISH

**A Python toolbox for the analysis of fluorescence in situ hybridization (FISH) microscopy images.**

[![codecov](https://codecov.io/gh/apiFISH/apiFISH/branch/development/graph/badge.svg?token=TSFJPBCANN)](https://codecov.io/gh/apiFISH/apiFISH)
[![Tests](https://github.com/apiFISH/apiFISH/actions/workflows/tests.yml/badge.svg?branch=development)](https://github.com/apiFISH/apiFISH/actions/workflows/tests.yml)

apiFISH provides tools for processing and analyzing fluorescence microscopy images, with a particular focus on single-molecule fluorescence in situ hybridization (smFISH) experiments.

Built on the foundations of [Big-FISH](https://github.com/fish-quant/big-fish), apiFISH brings together image processing, segmentation, spot detection, spatial analysis, and visualization tools in a Python package.

The package is designed for researchers analyzing microscopy datasets and for developers building reproducible image-analysis workflows.

**Resources:** [Documentation](https://apifish.readthedocs.io/en/latest/) · [Tutorials](https://apifish.readthedocs.io/en/latest/getting_started/tutorials.html) · [Source code](https://github.com/apiFISH/apiFISH) · [Issues](https://github.com/apiFISH/apiFISH/issues)

## Features

apiFISH includes tools for:

- **Image input and preprocessing:** reading microscopy images, normalization, filtering, and image projection.
- **Segmentation:** identification of nuclei and cells in fluorescence images.
- **Spot detection:** detection and characterization of fluorescent spots.
- **Spatial analysis:** colocalization, cluster detection, and related analyses.
- **Cell-level analysis:** associating detected spots with segmented cells and nuclei.
- **Image registration:** tools for comparing or combining microscopy images.
- **Visualization:** displaying images, segmentation masks, detections, and analysis results.

The package provides modular Python functions that can be combined into analysis workflows.

## Installation

### Requirements

apiFISH is a Python package. Its dependencies include NumPy, SciPy, scikit-image, scikit-learn, pandas, Matplotlib, Astropy, tifffile, and mrc.

The package also declares TensorFlow and TensorFlow Addons as dependencies for functionality involving deep-learning-based segmentation.

**Python compatibility:** The project's current development configuration uses Python 3.9. Some dependencies have restrictive version requirements, so Python 3.9 is the recommended starting point for a new analysis environment. Compatibility with newer Python versions should be verified against the dependency versions in `pyproject.toml`.

### Install from PyPI

Create a dedicated Python environment to avoid conflicts with other scientific software.

Using [uv](https://docs.astral.sh/uv/):

```bash
uv venv --python 3.9 .venv
source .venv/bin/activate
uv pip install apifish
```

Alternatively, using Conda:

```bash
conda create -n apifish python=3.9
conda activate apifish
pip install apifish
```

Installation may require additional attention to the compatibility of TensorFlow, TensorFlow Addons, and scikit-image. See the [installation documentation](https://apifish.readthedocs.io/en/latest/getting_started/installation.html) for further information.

### Install from source

To work with the development version:

```bash
git clone https://github.com/apiFISH/apiFISH.git
cd apiFISH
git checkout development
```

Create and activate an environment:

```bash
uv venv --python 3.9 .venv
source .venv/bin/activate
```

Install the package in editable mode:

```bash
uv pip install -e .
```

Editable installation allows changes to the source code to be reflected without reinstalling the package.

## Getting started

apiFISH provides Python functions that can be used individually or combined into image-analysis workflows.

The documentation includes Jupyter notebook tutorials covering the main processing steps:

1. Reading and writing microscopy images.
2. Image normalization and filtering.
3. Image projection into two dimensions.
4. Segmentation of nuclei and cells.
5. Detection of fluorescent spots.
6. Extraction of cell-level analysis results.

These tutorials provide practical examples of the package's functionality.

**[Explore the tutorials](https://apifish.readthedocs.io/en/latest/getting_started/tutorials.html)**

## Documentation

The full documentation is available at:

**https://apifish.readthedocs.io/**

It includes installation instructions, tutorials, an API reference, and information for contributors.

The documentation source files are located in `docs/source/` and are generated using Sphinx.

## Development

Development takes place on GitHub:

**https://github.com/apiFISH/apiFISH**

The `development` branch is used for ongoing development. Contributions should normally be submitted through pull requests.

### Contributing

Contributions are welcome, including bug reports, improvements to documentation, new functionality, and fixes to existing code.

To contribute:

1. Check the [existing issues](https://github.com/apiFISH/apiFISH/issues) or open a new issue describing the proposed change.
2. Fork the repository or create a development branch, as appropriate.
3. Make your changes and add or update relevant tests and documentation.
4. Submit a [pull request](https://github.com/apiFISH/apiFISH/pulls) describing the changes.

For additional information, consult the [contributor documentation](https://apifish.readthedocs.io/en/latest/development/contributing_to_apiFISH.html).

### Building the documentation locally

The documentation can be built using [uv](https://docs.astral.sh/uv/) and Sphinx.

The repository provides a `build_doc.sh` script that creates a dedicated Python environment, installs the documentation dependencies, and generates the HTML documentation.

**Prerequisites**

- Git
- uv
- A web browser

Clone the repository and switch to the development branch:

```bash
git clone https://github.com/apiFISH/apiFISH.git
cd apiFISH
git checkout development
```

Run the documentation build script:

```bash
./build_doc.sh
```

The script:

- Creates `.venv-docs/` using Python 3.11.
- Installs the packages listed in `docs/requirements.txt`.
- Installs apiFISH in editable mode without its runtime dependencies.
- Builds the documentation with Sphinx.
- Saves the HTML output to `docs/build/html/`.

The documentation environment is preserved between builds, making subsequent builds faster.

To open the generated documentation:

```bash
xdg-open docs/build/html/index.html
```

On Linux systems with `xdg-open`, you can also build and open the documentation using:

```bash
./build_doc.sh --open
```

To rebuild after changing documentation files or Python docstrings, simply rerun:

```bash
./build_doc.sh
```

**Checking documentation warnings**

For stricter validation, run:

```bash
.venv-docs/bin/python -m sphinx \
    -b html -n -W --keep-going \
    docs/source docs/build/html
```

This treats Sphinx warnings as build errors.

The documentation currently builds successfully, although some warnings remain concerning image references, internal links, and theme configuration. These warnings do not prevent normal HTML generation.

**Cleaning the documentation environment**

To remove generated HTML files and the documentation environment:

```bash
rm -rf docs/build .venv-docs
```

The next build will recreate them.

### Testing

Tests are maintained in the repository, and automated checks are configured through GitHub Actions.

See the [GitHub Actions workflows](https://github.com/apiFISH/apiFISH/actions) for the current automated test status.

When contributing code, run the tests relevant to your changes and ensure that new functionality is accompanied by appropriate tests.

## Support and reporting issues

For bug reports, feature requests, or questions about the software, please use the [GitHub issue tracker](https://github.com/apiFISH/apiFISH/issues).

When reporting a bug, include the apiFISH version, Python version, operating system, a description of the problem, and a minimal example or traceback when possible.

## Acknowledgments

apiFISH builds on the work of the [Big-FISH](https://github.com/fish-quant/big-fish) project and its contributors.

We acknowledge the developers of the open-source scientific Python libraries on which apiFISH depends.

## Citation

If you use apiFISH in published research, please cite the software repository and acknowledge the underlying Big-FISH project where appropriate.

A formal software citation will be added here when the corresponding publication or archived software release is available.

## License

See the [LICENSE](https://github.com/apiFISH/apiFISH/blob/development/LICENSE) file for the terms governing use and distribution of apiFISH.
