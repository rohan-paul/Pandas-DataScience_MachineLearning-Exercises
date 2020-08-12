### Difference-1 - high-level points.

pip is a package manager that facilitates installation, upgrade, and uninstallation of **python packages**. It also works with virtual **python** environments.

conda is a package manager for **any software** (installation, upgrade and uninstallation). It also works with virtual **system** environments.

One of the goals with the design of conda is to facilitate package management for the entire software stack required by users, of which one or more python versions may only be a small part. This includes low-level libraries, such as linear algebra, compilers, such as mingw on Windows, editors, version control tools like Hg and Git, or _whatever else requires distribution and management_.

For version management, pip allows you to switch between and manage multiple **python** environments.

Conda allows you to switch between and manage **multiple general purpose environments** across which multiple other things can vary in version number, like C-libraries, or compilers, or test-suites, or database engines and so on.

## pip

- Python packages only.
- Compiles everything from source. **EDIT: pip now installs binary wheels, if they are available.**
- Blessed by the core Python community (i.e., Python 3.4+ includes code that automatically bootstraps pip).

## conda

- Python agnostic. The main focus of existing packages are for Python, and indeed Conda itself is written in Python, but you can also have Conda packages for C libraries, or R packages, or really anything.
- Installs binaries. There is a tool called `conda build` that builds packages from source, but `conda install` itself installs things from already built Conda packages.
- External. Conda is the package manager of Anaconda, the Python distribution provided by Continuum Analytics, but it can be used outside of Anaconda too. You can use it with an existing Python installation by pip installing it (though this is not recommended unless you have a good reason to use an existing installation).

In both cases:

- Written in Python
- Open source (Conda is BSD and pip is MIT)

Conda is not Windows-centric, but on Windows it is by far the superior solution currently available when complex scientific packages requiring compilation are required to be installed and managed.

I want to weep when I think of how much time I have lost trying to compile many of these packages via pip on Windows, or debug failed `pip install` sessions when compilation was required.

As a final point, Continuum Analytics also hosts (free) [binstar.org][1] (now called [anaconda.org][2]) to allow regular package developers to create their own custom (built!) software stacks that their package-users will be able to `conda install` from.

[1]: https://binstar.org
[2]: https://anaconda.org/

---

Quoting from the [Conda blog](http://web.archive.org/web/20170415041123/www.continuum.io/blog/developer-blog/python-packages-and-environments-conda):

> Having been involved in the python world for so long, we are all aware of pip, easy_install, and virtualenv, but these tools did not meet all of our specific requirements. The main problem is that they are focused around Python, neglecting non-Python library dependencies, such as HDF5, MKL, LLVM, etc., which do not have a setup.py in their source code and also do not install files into Python’s site-packages directory.

**So Conda is a packaging tool and installer that aims to do more than what `pip` does; handle library dependencies _outside_ of the Python packages as well as the Python packages themselves. Conda also creates a virtual environment, like `virtualenv` does.**

As such, Conda should be compared to [Buildout](http://www.buildout.org/en/latest/) perhaps, another tool that lets you handle both Python and non-Python installation tasks.

**Because Conda introduces a new packaging format, you cannot use `pip` and Conda interchangeably; `pip` cannot install the Conda package format. You can use the two tools side by side (by installing `pip` with `conda install pip`) but they do not interoperate either.**

Since writing this answer, Anaconda has published a [new page on _Understanding Conda and Pip_](https://www.anaconda.com/understanding-conda-and-pip/), which echoes this as well:

> This highlights a key difference between conda and pip. Pip installs Python packages whereas conda installs packages which may contain software written in any language. For example, before using pip, a Python interpreter must be installed via a system package manager or by downloading and running an installer. Conda on the other hand can install Python packages as well as the Python interpreter directly.

and further on

> Occasionally a package is needed which is not available as a conda package but is available on PyPI and can be installed with pip. In these cases, it makes sense to try to use both conda and pip.

https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda

https://www.anaconda.com/blog/understanding-conda-and-pip
