### What does conda do when “solving environment”

**[SO question](https://stackoverflow.com/questions/51753988/what-does-conda-do-when-solving-environment)**

Whenever I run `conda install/remove/update <package>`, it tells me it's "Solving environment" for some time before telling me the list of things it's going to download/install/update. Presumably it's looking for dependencies for `<package>`, but why does it sometimes _remove_ packages after doing this operation? For example, as I was trying to install Mayavi, it decided it needed to remove Anaconda Navigator.

Furthermore it does not provide an option to perform only a subset of the suggested operations. Is there a way to specify that I don't want a package removed?

**Ans -**

You can add `--debug` option to the conda command and see the output from console(or terminal). For example, type `conda update --debug numpy`.
From the output, we can see that the client requests `repodata.json` from channel list and do some computation locally in the `Solving Environment` Step.
