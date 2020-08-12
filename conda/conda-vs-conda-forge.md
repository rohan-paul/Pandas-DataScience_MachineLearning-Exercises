### Should conda, or conda-forge be used for Python environments?

**Conda and conda-forge are both Python package managers. What is the appropriate choice when a package exists in both repositories? Django, for example, can be installed with either, but the difference between the two is several dependencies (conda-forge has many more).**

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

1. Packages on `conda-forge` _may_ be more up-to-date than those on the `defaults` channel
2. There are packages on the `conda-forge` channel that aren't available from `defaults`
