# stactools-nisar

`stactools-nisar` is a `stactools` plugin that will generate STAC Items from NASA-ISRO SAR (NISAR) HDF5 products.

## What is NISAR?

NISAR (NASA-ISRO Synthetic Aperture Radar) is a joint NASA and ISRO Earth-observing mission using synthetic aperture radar to measure changes in Earth’s land and ice surfaces and enable applications such as hazards, ecosystems, and agriculture.

NASA mission page: https://science.nasa.gov/mission/nisar/

## What `stactools-nisar` will do (when complete)

When complete, `stactools-nisar` will:

1. Ingest NISAR GCOV and RSLC HDF5 files (starting with L-band products).
2. Extract product metadata (e.g., orbit identifiers, frequency grouping, polarization, incidence angle).
3. Emit a valid STAC Item JSON that is compatible with STAC tooling and implements the relevant STAC extensions (notably SAR).

## Current status

Namespace placeholder — v0.1.0 coming soon.

This repository currently exists to claim the `stactools-nisar` name on GitHub and PyPI and provide a minimal, working installable stub.

## Install (stub)

```bash
pip install stactools-nisar
