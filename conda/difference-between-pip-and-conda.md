Quoting from the [Conda blog](http://web.archive.org/web/20170415041123/www.continuum.io/blog/developer-blog/python-packages-and-environments-conda):

> Having been involved in the python world for so long, we are all aware of pip, easy_install, and virtualenv, but these tools did not meet all of our specific requirements. The main problem is that they are focused around Python, neglecting non-Python library dependencies, such as HDF5, MKL, LLVM, etc., which do not have a setup.py in their source code and also do not install files into Python’s site-packages directory.

So Conda is a packaging tool and installer that aims to do more than what `pip` does; handle library dependencies _outside_ of the Python packages as well as the Python packages themselves. Conda also creates a virtual environment, like `virtualenv` does.

As such, Conda should be compared to [Buildout](http://www.buildout.org/en/latest/) perhaps, another tool that lets you handle both Python and non-Python installation tasks.

Because Conda introduces a new packaging format, you cannot use `pip` and Conda interchangeably; `pip` cannot install the Conda package format. You can use the two tools side by side (by installing `pip` with `conda install pip`) but they do not interoperate either.

Since writing this answer, Anaconda has published a [new page on _Understanding Conda and Pip_](https://www.anaconda.com/understanding-conda-and-pip/), which echoes this as well:

> This highlights a key difference between conda and pip. Pip installs Python packages whereas conda installs packages which may contain software written in any language. For example, before using pip, a Python interpreter must be installed via a system package manager or by downloading and running an installer. Conda on the other hand can install Python packages as well as the Python interpreter directly.

and further on

> Occasionally a package is needed which is not available as a conda package but is available on PyPI and can be installed with pip. In these cases, it makes sense to try to use both conda and pip.

https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda
