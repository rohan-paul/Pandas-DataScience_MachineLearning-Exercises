#### There are 3 ways to Install Jupyterlab:

1. Conda (that requires you to install Anaconda first, follow this Tutorial to do so!)
2. Pip
3. Pipenv

**Step 1 – Install Jupyterlab using Conda**

Assuming you have Anaconda installed, simply run:

`conda install -c conda-forge jupyterlab`

**Step 2 – Install Jupyterlab using Pip**

**This is what I followed in my Ubuntu 20.04**

**To install Jupyterlab using Pip, simply run:**

_**pip install jupyterlab**_

**Step 3 – Install Jupyterlab using Pipenv**

For Pipenv we need to run:

```
pipenv install jupyterlab
pipenv shell

```

Or from a Git Checkout:

```
pipenv install git+git://github.com/jupyterlab/jupyterlab.git#egg=jupyterlab
pipenv shell
Step 4 – Starting Jupyterlab

```

### To start Jupyterlab you simply run:

**`jupyter lab`**

[https://www.ceos3c.com/open-source/install-jupyterlab-on-ubuntu-18-04/](https://www.ceos3c.com/open-source/install-jupyterlab-on-ubuntu-18-04/)

#### the-version-of-my-jupyter-notebook

```
jupyter notebook --version
```

And if you simply you can run this:

`jupyter --version`

Then all the Jupyterlab related tool's version (including jupyter-lab) will be printed.
