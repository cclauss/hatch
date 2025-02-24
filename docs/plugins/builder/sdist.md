# Source distribution builder

-----

A source distribution, or `sdist`, is an archive of Python "source code". Although largely unspecified, by convention it should include everything that is required to build a [wheel](wheel.md) without making network requests.

## Configuration

The builder plugin name is `sdist`.

=== ":octicons-file-code-16: pyproject.toml"

    ```toml
    [tool.hatch.build.targets.sdist]
    ```

=== ":octicons-file-code-16: hatch.toml"

    ```toml
    [build.targets.sdist]
    ```

## Options

| Option | Default | Description |
| --- | --- | --- |
| `core-metadata-version` | `"2.1"` | The version of [core metadata](https://packaging.python.org/specifications/core-metadata/) to use |
| `support-legacy` | `false` | Whether or not to include a `setup.py` file to support legacy installation mechanisms |

## Versions

| Version | Description |
| --- | --- |
| `standard` (default) | The latest conventional format |

## Default file selection

When the user has not set any [file selection](../../config/build.md#file-selection) options, all files that are not [ignored by your VCS](../../config/build.md#vcs) will be included.

## Reproducibility

[Reproducible builds](../../config/build.md#reproducible-builds) are supported.

## Build data

This is data that can be modified by [build hooks](../build-hook/reference.md).

| Data | Default | Description |
| --- | --- | --- |
| `dependencies` | | Extra [project dependencies](../../config/metadata.md#required) |
