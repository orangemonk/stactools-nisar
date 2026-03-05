# Contributing to stactools-nisar

Thanks for your interest in contributing.

This repository implements a `stactools` plugin under the `stactools`
namespace package (`stactools.nisar`). Because `stactools` is a
namespace package, **do not add** `src/stactools/__init__.py`.

## Development environment (WSL Ubuntu + uv)

1.  Clone the repository:

``` bash
git clone https://github.com/OrangeMonk/stactools-nisar.git
cd stactools-nisar
```

2.  Verify that `uv` is installed:

``` bash
uv --version
```

3.  Create and synchronize the project environment:

``` bash
uv sync
```

4.  Install the project in editable mode:

``` bash
uv run python -m pip install -e .
```

## Quick verification (stub)

Verify that the plugin command is registered.

``` bash
uv run stac nisar
```

Expected output:

    stactools-nisar plugin loaded

Verify that the package imports correctly.

``` bash
uv run python -c "import stactools.nisar; print('OK')"
```

Expected output:

    OK

## Running tests

Run the test suite with:

``` bash
uv run pytest
```

## Code quality (optional but recommended)

If linting tools are configured, run them before submitting a pull
request.

``` bash
uv run ruff check .
```

## Submitting a pull request

1.  Create a new branch:

``` bash
git checkout -b your-branch-name
```

2.  Make your changes and add tests where appropriate.

3.  Run verification checks:

``` bash
uv run pytest
uv run stac nisar
```

4.  Commit and push your changes:

``` bash
git add -A
git commit -m "Describe your change"
git push -u origin your-branch-name
```

5.  Open a Pull Request on GitHub.

## Reporting security issues

If you discover a security vulnerability, please do not open a public
issue.\
Instead contact the maintainers through the contact email listed in the
GitHub organization profile.

