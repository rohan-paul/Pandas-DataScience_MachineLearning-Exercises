### Do separate Anaconda environments install the same package twice, taking up twice the storage?

If I have two separate Anaconda Environments, and am installing two packages that are the same in each environment, do they install twice, and take up twice the storage?

```
conda create --name myenv1

conda create --name myenv2

conda activate myenv1

conda install matplotlib

deactivate

conda activate myenv2

conda install matplotlib
```

**No it doesn't take up twice the storage.**

Environments by default are created in the `envs` folder under the directory you installed anaconda in. For me that is `$HOME/anaconda3`. After each install you want to run `du -sh $HOME/anaconda3/envs` to see a summary of disk space used in human readable format.

```
$ du -sh $HOME/anaconda3/envs
4.0K    /root/anaconda3/envs

$ conda create --name myenv1 -y
$ conda create --name myenv2 -y
$ conda install matplotlib -n myenv1 -y

$ du -sh $HOME/anaconda3/envs
338M    /root/anaconda3/envs


$ conda install matplotlib -n myenv2 -y

$ du -sh $HOME/anaconda3/envs
357M    /root/anaconda3/envs
```

19M more was used, but not double.

Now the question is how do they avoid doubling the space, looking and the envs directory, I don't see any symlinks anywhere. So I looked at some files under myenv2:

```
$ ls -lh /root/anaconda3/envs/myenv2/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf
-rw-rw-r--. 3 root root 688K Jul  1 06:19 /root/anaconda3/envs/myenv2/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/DejaVuSans-Bold.ttf
```

The '3' after the permissions and before the file and group owner is the number of hard-links associated with a file. Normally a file has only one. Each environment must create another hard-link to the same file.

https://stackoverflow.com/questions/57717410/do-separate-anaconda-environments-install-the-same-package-twice-taking-up-twic
