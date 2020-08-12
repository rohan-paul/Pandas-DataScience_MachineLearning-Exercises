**A key difference between the two tools is that conda has the ability to create isolated environments that can contain different versions of Python and/or the packages installed in them. This can be extremely useful when working with data science tools as different tools may contain conflicting requirements which could prevent them all being installed into a single environment. Pip has no built in support for environments but rather depends on other tools like virtualenv or venv to create isolated environments. Tools such as pipenv, poetry, and hatch wrap pip and virtualenv to provide a unified method for working with these environments.**

**Next to the root environment, you can create as many additional environments as you want. And the whole point is that these additional environments can contain different versions of Pythons and other packages. So it means that, for example, if your precious little application is not working anymore in the newest, state-of-the-art environment you’ve just set up, you can always go “back” and use some another version(s) of some packages (including Python – Python itself is a package**

https://www.anaconda.com/blog/understanding-conda-and-pip

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#:~:text=With%20conda%2C%20you%20can%20create,also%20share%20an%20environment%20file.

With conda, you can create, export, list, remove, and update environments that have different versions of Python and/or packages installed in them. Switching or moving between environments is called activating the environment. You can also share an environment file.

`conda activate` and `conda deactivate` only work on conda 4.6 and later versions. For conda versions prior to 4.6, run:

Windows: `activate` or `deactivate`

Linux and macOS: `source activate` or `source deactivate`

### create a Python virtual environment

`conda create --name env_name python=3.7`

The above line literally says: Create an environment using the conda create command whose name is env_name (you can choose any name) that runs on python=3.7

#### Command To Make exact copy of an environment

**conda create --clone py35 --name py35-2**

#### Downloading from specific Channel

When I run below to install [**jupyterlab/debugger**](https://github.com/jupyterlab/debugger)

`conda create -n jupyterlab-debugger -c conda-forge xeus-python=0.8.0 notebook=6 jupyterlab=2 ptvsd nodejs`

**In above the "-c" stands for channel - meaning with above command jupyterlab-debugger will be downloaded from conda-forge channel**

Then activate that with `conda activate jupyterlab-debugger`

Then, run the following command to install the extension:

`jupyter labextension install @jupyterlab/debugger`

### To delete or remove the environment, type the following in your terminal:

`conda remove --name env_name --all`

#### I installed several conda packages in `/usr/local/pkgs`, and created a new environment with `conda create --name env1`. Will this environment by default include all the packages in `/usr/local/pkgs`, or will it include only the packages that are shipped by default with conda?

**And the ans to above is**

No, it does NOT automatically include all those packages. If you want it to, you can use

**`conda create --name env1 --clone base`**

**But it's generally not recommended to clone **base** since it includes additional packages only **base** needs.**

You can check what is installed in an env with

    conda list --name env1

OR after activating the env

```
conda activate envname
conda list
```
