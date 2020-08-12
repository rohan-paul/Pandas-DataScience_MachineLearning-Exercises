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
