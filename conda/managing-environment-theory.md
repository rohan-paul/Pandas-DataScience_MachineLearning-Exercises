### What is an Environment

An environment is a way of starting with a new Python installation, that doesn't look at your already installed packages. In this way, it simulates having a fresh install of Python. If two applications require different versions of Python, you can simply create different environments for them. If you start from a fresh environment and install as you go, you are able to generate a list of all packages installed in the environment so that others can easily duplicate it.

There are few steps to using an environment (with a third step needed if you want to use Jupyter notebooks)

- Creating the environment, either from scratch (a new project) or from a yaml file (duplicating an environment)
- Activating the environment for use.
- Register the environment with Jupyter.
- To leave an environment, we have to deactivate it.

#### Anaconda Python: where are the virtual environments stored?

Simple Ans - Your environments are located in `**Anaconda3\envs\<yourEnv_directory>\**`

You can also run `conda info` which will give you details

![](assets/2020-08-13-02-26-34.png)

**A key difference between the two tools is that conda has the ability to create isolated environments that can contain different versions of Python and/or the packages installed in them. This can be extremely useful when working with data science tools as different tools may contain conflicting requirements which could prevent them all being installed into a single environment. Pip has no built in support for environments but rather depends on other tools like virtualenv or venv to create isolated environments. Tools such as pipenv, poetry, and hatch wrap pip and virtualenv to provide a unified method for working with these environments.**

**Next to the root environment, you can create as many additional environments as you want. And the whole point is that these additional environments can contain different versions of Pythons and other packages. So it means that, for example, if your precious little application is not working anymore in the newest, state-of-the-art environment you’ve just set up, you can always go “back” and use some another version(s) of some packages (including Python – Python itself is a package**

https://www.anaconda.com/blog/understanding-conda-and-pip

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#:~:text=With%20conda%2C%20you%20can%20create,also%20share%20an%20environment%20file.

With conda, you can create, export, list, remove, and update environments that have different versions of Python and/or packages installed in them. Switching or moving between environments is called activating the environment. You can also share an environment file.

---
