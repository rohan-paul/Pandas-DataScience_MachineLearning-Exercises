**A key difference between the two tools is that conda has the ability to create isolated environments that can contain different versions of Python and/or the packages installed in them. This can be extremely useful when working with data science tools as different tools may contain conflicting requirements which could prevent them all being installed into a single environment. Pip has no built in support for environments but rather depends on other tools like virtualenv or venv to create isolated environments. Tools such as pipenv, poetry, and hatch wrap pip and virtualenv to provide a unified method for working with these environments.**

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

So when I run below to install [**jupyterlab/debugger**](https://github.com/jupyterlab/debugger)

`conda create -n jupyterlab-debugger -c conda-forge xeus-python=0.8.0 notebook=6 jupyterlab=2 ptvsd nodejs`

It means I am creating an exact copy of **conda-forge**

Then activate that with `conda activate jupyterlab-debugger`

Then, run the following command to install the extension:

`jupyter labextension install @jupyterlab/debugger`

### To delete or remove the environment, type the following in your terminal:

`conda remove --name env_name --all`
