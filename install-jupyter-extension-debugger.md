```
pip install xeus-python==0.7.1
pip install ptvsd
```

The debugger front-end can be installed as a JupyterLab extension. run:

`jupyter labextension install @jupyterlab/debugger`

In the back-end, a kernel implementing the Jupyter Debug Protocol (which will be detailed in the next section) is required. The only kernel implementing this protocol, for now, is xeus-python a new Jupyter kernel for the Python programming language. (Support for the debugger protocol in ipykernel is also on the roadmap).

`conda install xeus-python -c conda-forge`

The first time I ran the above in Ubuntu 20.04 - took almost 5 mintes to finish

#### Reading

https://blog.jupyter.org/a-visual-debugger-for-jupyter-914e61716559

https://towardsdatascience.com/3-must-have-jupyterlab-2-0-extensions-41024fe455cc

https://github.com/jupyterlab/debugger
