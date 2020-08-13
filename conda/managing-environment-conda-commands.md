### create a Python virtual environment

`conda create --name env_name python=3.7`

The above line literally says: Create an environment using the conda create command whose name is env_name (you can choose any name) that runs on python=3.7

#### Command To Make exact copy of an environment

**conda create --clone py35 --name py35-2**

### Downloading from specific Channel while creating a new environment

When I run below to install [**jupyterlab/debugger**](https://github.com/jupyterlab/debugger)

`conda create -n jupyterlab-debugger -c conda-forge xeus-python=0.8.0 notebook=6 jupyterlab=2 ptvsd nodejs`

**In above the "-c" stands for channel - meaning with above command jupyterlab-debugger will be downloaded from conda-forge channel**

**Then activate that with `conda activate jupyterlab-debugger`**

Then, run the following command to install the extension:

`jupyter labextension install @jupyterlab/debugger`

---

### Pre and Post Activation python bin file location

**First note before activating any conda environment (i.e. when I am in PIP environment) if you run below**

`which python`

It would give `/usr/bin/python`

**Then activate a conda environment e.g. with `conda activate jupyterlab-debugger`**

And run `which python`

And it would give

```
(jupyterlab-debugger) paul@paul-B85M-D3H:~$ which python
/home/paul/anaconda3/envs/jupyterlab-debugger/bin/python
```

### Activating my new environment

**For work on conda 4.6 and later versions. **

`conda activate` and `conda deactivate`

**For conda versions prior to 4.6, run:**

Windows: `activate` or `deactivate`

Linux and macOS: `source activate` or `source deactivate`

### Connecting my new environment with Jupyter

If you want Jupyter notebooks to see your new environment, you need a couple of extra instructions. Jupyter sees the different environments as different kernels. Once we create a new environment, we need to tell Jupyter that it is there:

**Note you'll want to do this in the new environment.**

**First we will need the ipykernel package**

**`(test_env) $ conda install ipykernel`**

This tells jupyter to take the current environment (test_env) and make a "kernel" option named "test kernel" in the kernel menu

**`(test_env) $ python -m ipykernel install --user --name myenv --display-name "test kernel"`**

For example if my newly created env name is **"jupyterlab-debugger"** I need to run the below command (which is slightly simplified version of the above)

`python -m ipykernel install --user --name=jupyterlab-debugger`

https://stackoverflow.com/a/53546634/1902852

https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084

---

### To delete or remove the environment, type the following in your terminal:

`conda remove --name env_name --all`

---

### Make my new environment exportable and usable by others

Now you want to make an environment.yaml file that will allow others to recreate the environment from scratch. To make this file, we use the export command and send the output to environment.yaml:

**while in test_env, export the packages used to an environment file**

**`(test_env) \$ conda env export > environment.yaml`**

Once we are done with the environment, we can deactivate and delete the environment:

**Leave the environment**

(test_env) \$ source deactivate

**Now we are no longer in test_env, we can delete it**

`$ conda env remove --name test_env`

### Making the environment again from the yaml file

If you have the yaml file (created from conda env export), then recreating the environment is a single command:

**`$ conda env create --file environment.yaml`**

Note that you don't need to supply the name of the new environment, as the yaml file also contains the name of the environment it saved. Make sure you don't give your environment an embarassing name, as everyone who recreates from the yaml file will see the name you used!

### Finding conda environments on your system

Of course, you may choose to deactivate your environment but keep it around for later. If you want to see the environments installed on your system, use

`$ conda env list`

https://kiwidamien.github.io/save-the-environment-with-conda-and-how-to-let-others-run-your-programs.html
