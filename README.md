# Skia python binding

[![CI](https://github.com/kyamagu/skia-python/actions/workflows/ci.yml/badge.svg)](https://github.com/kyamagu/skia-python/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/skia-python.svg)](https://badge.fury.io/py/skia-python)

Python binding to [Skia Graphics Library](https://skia.org/).

- Binding based on [pybind11](https://github.com/pybind/pybind11).

## Install

Binary package is available on PyPI:

```bash
pip install skia-python
```

Supported platforms: Python 3.8-3.13 (CPython) on

- Linux x86_64, aarch64
- macOS x86_64, arm64
- Windows x86_64

For Linux platforms, there must be OpenGL and fontconfig installed:

```bash
apt-get install libfontconfig1 libgl1-mesa-glx libgl1-mesa-dri
```

Or:

```bash
yum install fontconfig mesa-libGL mesa-dri-drivers
```

For unsupported environment, check the [build instruction](https://kyamagu.github.io/skia-python/install.html).

## Examples

- [Showcase](https://github.com/kyamagu/skia-python/blob/main/notebooks/Showcase.ipynb)
- [Canvas Overview](https://github.com/kyamagu/skia-python/blob/main/notebooks/Canvas-Overview.ipynb)
- [Canvas Creation](https://github.com/kyamagu/skia-python/blob/main/notebooks/Canvas-Creation.ipynb)
- [Path Overview](https://github.com/kyamagu/skia-python/blob/main/notebooks/Path-Overview.ipynb)
- [Paint Overview](https://github.com/kyamagu/skia-python/blob/main/notebooks/Paint-Overview.ipynb)
- [Python Image I/O](https://github.com/kyamagu/skia-python/blob/main/notebooks/Python-Image-IO.ipynb)
- [Drawing Texts](https://github.com/kyamagu/skia-python/blob/main/notebooks/Drawing-Texts.ipynb)

## Documentation

https://kyamagu.github.io/skia-python

- [Tutorial](https://kyamagu.github.io/skia-python/tutorial/)
- [Reference](https://kyamagu.github.io/skia-python/reference.html)

- For information about changes after `m116`, and tips on migration from `m87`: [README.m116](relnotes/README.m116.md),
  [README.m117](relnotes/README.m117.md), [README.m118](relnotes/README.m118.md), [README.m119](relnotes/README.m119.md),
  [README.m120](relnotes/README.m120.md), [README.m121](relnotes/README.m121.md), [README.m122](relnotes/README.m122.md),
  [README.m123](relnotes/README.m123.md), [README.m124](relnotes/README.m124.md), [README.m125](relnotes/README.m125.md),
  [README.m126](relnotes/README.m126.md), [README.m127](relnotes/README.m127.md), [README.m128](relnotes/README.m128.md),
  [README.m129](relnotes/README.m129.md), [README.m130](relnotes/README.m130.md), [README.m131](relnotes/README.m131.md),
  [README.m132](relnotes/README.m132.md), [README.m133](relnotes/README.m133.md), [README.m134](relnotes/README.m134.md).

## Contributing

Feel free to [post an issue](https://github.com/kyamagu/skia-python/issues) or [PR](https://github.com/kyamagu/skia-python/pulls).
