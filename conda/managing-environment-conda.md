https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#:~:text=With%20conda%2C%20you%20can%20create,also%20share%20an%20environment%20file.

With conda, you can create, export, list, remove, and update environments that have different versions of Python and/or packages installed in them. Switching or moving between environments is called activating the environment. You can also share an environment file.

`conda activate` and `conda deactivate` only work on conda 4.6 and later versions. For conda versions prior to 4.6, run:

Windows: `activate` or `deactivate`

Linux and macOS: `source activate` or `source deactivate`

### Important commands

You can run `conda info --envs`, and that will show the paths to all your environments.

#### Display Conda environment information

`conda info`

![](assets/2020-08-12-20-11-56.png)

**List all existing environments**

`conda env list`

![](assets/2020-08-12-20-16-38.png)
