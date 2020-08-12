### Should conda, or conda-forge be used for Python environments?

**Conda and conda-forge are both Python package managers. What is the appropriate choice when a package exists in both repositories? Django, for example, can be installed with either, but the difference between the two is several dependencies (conda-forge has many more).**

The short answer is that, in my experience generally, it doesn't matter which you use.

The long answer:

So `conda-forge` is an additional channel from which packages may be installed. In this sense, it is not any more special than the default channel, or any of the other hundreds (thousands?) of channels that people have posted packages to. You can add your own channel if you sign up at https://anaconda.org and upload your own Conda packages.

**Here we need to make the distinction, which I think you're not clear about from your phrasing in the question, between `conda`, the cross-platform package manager, and `conda-forge`, the package channel.**

Anaconda Inc. (formerly Continuum IO), the main developers of the `conda` software, also maintain a separate channel of packages, which is the default when you type `conda install packagename` without changing any options.

---

To see your channel configuration, you can write:

    conda config --show channels

You can control the order that channels are searched with `conda config`. You can write:

    conda config --add channels some-channel

to add the channel `some-channel` to the top of the `channels` configuration list. This gives `some-channel` the highest priority. Priority determines ([in part](http://conda.pydata.org/docs/channels.html)) which channel is selected when more than one channel has a particular package. To add the channel to the end of the list and give it the lowest priority, type

    conda config --append channels some-channel

If you would like to remove the channel that you added, you can do so by writing

    conda config --remove channels some-channel

See

    conda config -h

for more options.

With all of that said, there are four main reasons to use the `conda-forge` channel instead of the `defaults` channel maintained by Anaconda:

1. Packages on `conda-forge` _may_ be more up-to-date than those on the `defaults` channel. The `conda-forge` channel is where you can find packages that have been built for conda but yet to be part of the official Anaconda distribution.
2. There are packages on the `conda-forge` channel that aren't available from `defaults`

#### Command to download from specific Channel

When I run below to install [**jupyterlab/debugger**](https://github.com/jupyterlab/debugger)

`conda create -n jupyterlab-debugger -c conda-forge xeus-python=0.8.0 notebook=6 jupyterlab=2 ptvsd nodejs`

**In above the "-c" stands for channel - meaning with above command jupyterlab-debugger will be downloaded from conda-forge channel**

Then activate that with `conda activate jupyterlab-debugger`

Then, run the following command to install the extension:

`jupyter labextension install @jupyterlab/debugger`
