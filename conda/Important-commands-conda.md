# Important commands

[The Official Doc for commands and its shorter aliases](https://docs.conda.io/projects/conda/en/latest/commands/install.html)

```
conda install [-h] [--revision REVISION] [-n ENVIRONMENT | -p PATH]
                     [-c CHANNEL] [--use-local] [--override-channels]
                     [--repodata-fn REPODATA_FNS] [--strict-channel-priority]
                     [--no-channel-priority] [--no-deps | --only-deps]
                     [--no-pin] [--copy] [-C] [-k] [--offline] [-d] [--json]
                     [-q] [-v] [-y] [--download-only] [--show-channel-urls]
                     [--file FILE] [--force-reinstall]
                     [--freeze-installed | --update-deps | -S | --update-all | --update-specs]
                     [-m] [--clobber] [--dev]
                     [package_spec [package_spec ...]]
```

From the above some of the most frequently used are

**-n, --name => Name of environment**

**-c, --channel** => channel to search for packages

### General Basic Commands

You can run `conda info --envs`, and that will show the paths to all your environments.

**Most recommended way to install any new package e.g. TensorFlow**

`conda install -c conda-forge tensorflow`

Because `**conda-forge**` channel has few benefits over the regular conda channel

**If you want to install a specific package inside a specific conda environment, you can use the following command.**

First activate the conda environment and then do:

```
conda install --name <conda_env_name> -c <channel_name> <package_name>

```

For a concrete example, let's assume that you want to install [chainer](http://chainer.org) from the _channel_ `anaconda` to an already created conda environment named `chainerenv`, then you can do:

`conda install --name chainerenv -c anaconda chainer`

#### Display Conda environment information

`conda info`

![](assets/2020-08-12-20-11-56.png)

**List all existing environments**

`conda env list`

![](assets/2020-08-12-20-16-38.png)

**Update conda to the current version**

`conda update conda`

### Environment management Related

**Create a new environment named py35, install Python 3.5**

`conda create --name py35 python=3.5`

**Activate AND DeActivate - the new environment to use it**

**For conda 4.6 and later versions.**

**`conda activate env-name` and `conda deactivate`**

**For conda versions prior to 4.6, run:**

Windows: `activate` or `deactivate`

Linux and macOS: `source activate` or `source deactivate`

**Make exact copy / clone of an environment**

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

### Some more reference

https://conda.io/projects/conda/en/latest/commands.html
