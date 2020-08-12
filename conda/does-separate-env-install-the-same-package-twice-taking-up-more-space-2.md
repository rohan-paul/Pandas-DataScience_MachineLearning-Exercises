### Do separate Anaconda environments install the same package twice, taking up twice the storage?

**Ans seems to be Yes, by noting the below case**

##### Installing [jupyterlab/debugger](https://github.com/jupyterlab/debugger) following official guide

It is generally recommended to create a new `conda` environment to install the dependencies:

```bash
conda create -n jupyterlab-debugger -c conda-forge xeus-python=0.8.0 notebook=6 jupyterlab=2 ptvsd nodejs
conda activate jupyterlab-debugger
```

Then, run the following command to install the extension:

```bash
jupyter labextension install @jupyterlab/debugger
```

#### Special Note

**And after running below command**

`conda create -n jupyterlab-debugger -c conda-forge xeus-python=0.8.0 notebook=6 jupyterlab=2 ptvsd nodejs`

**I got a very long list of packages to be installed like below**

```

Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan

environment location: /home/paul/anaconda3/envs/jupyterlab-debugger

added / updated specs: - jupyterlab=2 - nodejs - notebook=6 - ptvsd - xeus-python=0.8.0

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    _libgcc_mutex-0.1          |      conda_forge           3 KB  conda-forge
    _openmp_mutex-4.5          |            1_gnu          22 KB  conda-forge
    argon2-cffi-20.1.0         |   py38h1e0a361_1          47 KB  conda-forge
    attrs-19.3.0               |             py_0          35 KB  conda-forge
    backcall-0.2.0             |     pyh9f0ad1d_0          13 KB  conda-forge
    backports-1.0              |             py_2           4 KB  conda-forge
    backports.functools_lru_cache-1.6.1|             py_0           8 KB  conda-forge
    bleach-3.1.5               |     pyh9f0ad1d_0         112 KB  conda-forge
    brotlipy-0.7.0             |py38h1e0a361_1000         346 KB  conda-forge
    ca-certificates-2020.6.20  |       hecda079_0         145 KB  conda-forge
    certifi-2020.6.20          |   py38h32f6830_0         151 KB  conda-forge
    cffi-1.14.1                |   py38h5bae8af_0         225 KB  conda-forge
    chardet-3.0.4              |py38h32f6830_1006         170 KB  conda-forge
    cryptography-3.0           |   py38h766eaa4_0         632 KB  conda-forge
    decorator-4.4.2            |             py_0          11 KB  conda-forge
    defusedxml-0.6.0           |             py_0          22 KB  conda-forge
    entrypoints-0.3            |py38h32f6830_1001          11 KB  conda-forge
    icu-67.1                   |       he1b5a44_0        12.9 MB  conda-forge
    idna-2.10                  |     pyh9f0ad1d_0          52 KB  conda-forge
    importlib-metadata-1.7.0   |   py38h32f6830_0          45 KB  conda-forge
    importlib_metadata-1.7.0   |                0           3 KB  conda-forge
    ipykernel-5.3.4            |   py38h23f93f0_0         166 KB  conda-forge
    ipython-7.17.0             |   py38h1cdfbd6_0         1.1 MB  conda-forge
    ipython_genutils-0.2.0     |             py_1          21 KB  conda-forge
    jedi-0.15.2                |           py38_0         766 KB  conda-forge
    jinja2-2.11.2              |     pyh9f0ad1d_0          93 KB  conda-forge
    json5-0.9.4                |     pyh9f0ad1d_0          20 KB  conda-forge
    jsonschema-3.2.0           |   py38h32f6830_1          90 KB  conda-forge
    jupyter_client-6.1.6       |             py_0          75 KB  conda-forge
    jupyter_core-4.6.3         |   py38h32f6830_1          71 KB  conda-forge
    jupyterlab-2.2.4           |             py_0         5.8 MB  conda-forge
    jupyterlab_server-1.2.0    |             py_0          25 KB  conda-forge
    ld_impl_linux-64-2.34      |       hc38a660_9         612 KB  conda-forge
    libffi-3.2.1               |    he1b5a44_1007          47 KB  conda-forge
    libgcc-ng-9.3.0            |      h24d8f2e_14         7.8 MB  conda-forge
    libgomp-9.3.0              |      h24d8f2e_14         374 KB  conda-forge
    libsodium-1.0.18           |       h516909a_0         339 KB  conda-forge
    libstdcxx-ng-9.3.0         |      hdf63c60_14         4.0 MB  conda-forge
    libuuid-2.32.1             |    h14c3975_1000          26 KB  conda-forge
    libuv-1.38.0               |       h516909a_0         924 KB  conda-forge
    markupsafe-1.1.1           |   py38h1e0a361_1          26 KB  conda-forge
    mistune-0.8.4              |py38h1e0a361_1001          54 KB  conda-forge
    nbconvert-5.6.1            |   py38h32f6830_1         488 KB  conda-forge
    nbformat-5.0.7             |             py_0          99 KB  conda-forge
    ncurses-6.2                |       he1b5a44_1         993 KB  conda-forge
    nodejs-14.8.0              |       h568c755_0        15.6 MB  conda-forge
    notebook-6.1.1             |   py38h32f6830_0         6.2 MB  conda-forge
    openssl-1.1.1g             |       h516909a_1         2.1 MB  conda-forge
    packaging-20.4             |     pyh9f0ad1d_0          32 KB  conda-forge
    pandoc-2.10.1              |       h516909a_0        19.3 MB  conda-forge
    pandocfilters-1.4.2        |             py_1           9 KB  conda-forge
    parso-0.8.0                |     pyh9f0ad1d_0          67 KB  conda-forge
    pexpect-4.8.0              |   py38h32f6830_1          80 KB  conda-forge
    pickleshare-0.7.5          |py38h32f6830_1001          13 KB  conda-forge
    pip-20.2.2                 |             py_0         1.1 MB  conda-forge
    prometheus_client-0.8.0    |     pyh9f0ad1d_0          44 KB  conda-forge
    prompt-toolkit-3.0.6       |             py_0         235 KB  conda-forge
    ptvsd-4.3.2                |   py38h516909a_1         4.6 MB  conda-forge
    ptyprocess-0.6.0           |          py_1001          15 KB  conda-forge
    pycparser-2.20             |     pyh9f0ad1d_2          94 KB  conda-forge
    pygments-2.6.1             |             py_0         683 KB  conda-forge
    pyopenssl-19.1.0           |             py_1          47 KB  conda-forge
    pyparsing-2.4.7            |     pyh9f0ad1d_0          60 KB  conda-forge
    pyrsistent-0.16.0          |   py38h1e0a361_0          90 KB  conda-forge
    pysocks-1.7.1              |   py38h32f6830_1          27 KB  conda-forge
    python-3.8.5               |h4d41432_2_cpython        71.0 MB  conda-forge
    python-dateutil-2.8.1      |             py_0         220 KB  conda-forge
    python_abi-3.8             |           1_cp38           4 KB  conda-forge
    pyzmq-19.0.2               |   py38ha71036d_0         492 KB  conda-forge
    readline-8.0               |       he28a2e2_2         281 KB  conda-forge
    requests-2.24.0            |     pyh9f0ad1d_0          47 KB  conda-forge
    send2trash-1.5.0           |             py_0          12 KB  conda-forge
    setuptools-49.3.1          |   py38h32f6830_0         938 KB  conda-forge
    six-1.15.0                 |     pyh9f0ad1d_0          14 KB  conda-forge
    sqlite-3.32.3              |       hcee41ef_1         1.4 MB  conda-forge
    terminado-0.8.3            |   py38h32f6830_1          23 KB  conda-forge
    testpath-0.4.4             |             py_0          85 KB  conda-forge
    tk-8.6.10                  |       hed695b0_0         3.2 MB  conda-forge
    tornado-6.0.4              |   py38h1e0a361_1         642 KB  conda-forge
    traitlets-4.3.3            |   py38h32f6830_1         134 KB  conda-forge
    urllib3-1.25.10            |             py_0          92 KB  conda-forge
    wcwidth-0.2.5              |     pyh9f0ad1d_1          33 KB  conda-forge
    webencodings-0.5.1         |             py_1          12 KB  conda-forge
    wheel-0.34.2               |             py_1          24 KB  conda-forge
    xeus-0.24.1                |       h4d8c418_0         8.9 MB  conda-forge
    xeus-python-0.8.0          |   py38hbf85e49_0        13.3 MB  conda-forge
    xz-5.2.5                   |       h516909a_1         343 KB  conda-forge
    zeromq-4.3.2               |       he1b5a44_3         326 KB  conda-forge
    zipp-3.1.0                 |             py_0          10 KB  conda-forge
    zlib-1.2.11                |    h516909a_1007         106 KB  conda-forge
    ------------------------------------------------------------
                                           Total:       190.7 MB

The following NEW packages will be INSTALLED:

\_libgcc_mutex conda-forge/linux-64::\_libgcc_mutex-0.1-conda_forge
\_openmp_mutex conda-forge/linux-64::\_openmp_mutex-4.5-1_gnu
argon2-cffi conda-forge/linux-64::argon2-cffi-20.1.0-py38h1e0a361_1
attrs conda-forge/noarch::attrs-19.3.0-py_0
backcall conda-forge/noarch::backcall-0.2.0-pyh9f0ad1d_0
backports conda-forge/noarch::backports-1.0-py_2
backports.functoo~ conda-forge/noarch::backports.functools_lru_cache-1.6.1-py_0
bleach conda-forge/noarch::bleach-3.1.5-pyh9f0ad1d_0
brotlipy conda-forge/linux-64::brotlipy-0.7.0-py38h1e0a361_1000
ca-certificates conda-forge/linux-64::ca-certificates-2020.6.20-hecda079_0
certifi conda-forge/linux-64::certifi-2020.6.20-py38h32f6830_0
cffi conda-forge/linux-64::cffi-1.14.1-py38h5bae8af_0
chardet conda-forge/linux-64::chardet-3.0.4-py38h32f6830_1006
cryptography conda-forge/linux-64::cryptography-3.0-py38h766eaa4_0
decorator conda-forge/noarch::decorator-4.4.2-py_0
defusedxml conda-forge/noarch::defusedxml-0.6.0-py_0
entrypoints conda-forge/linux-64::entrypoints-0.3-py38h32f6830_1001
icu conda-forge/linux-64::icu-67.1-he1b5a44_0
idna conda-forge/noarch::idna-2.10-pyh9f0ad1d_0
importlib-metadata conda-forge/linux-64::importlib-metadata-1.7.0-py38h32f6830_0
importlib_metadata conda-forge/noarch::importlib_metadata-1.7.0-0
ipykernel conda-forge/linux-64::ipykernel-5.3.4-py38h23f93f0_0
ipython conda-forge/linux-64::ipython-7.17.0-py38h1cdfbd6_0
ipython_genutils conda-forge/noarch::ipython_genutils-0.2.0-py_1
jedi conda-forge/linux-64::jedi-0.15.2-py38_0
jinja2 conda-forge/noarch::jinja2-2.11.2-pyh9f0ad1d_0
json5 conda-forge/noarch::json5-0.9.4-pyh9f0ad1d_0
jsonschema conda-forge/linux-64::jsonschema-3.2.0-py38h32f6830_1
jupyter_client conda-forge/noarch::jupyter_client-6.1.6-py_0
jupyter_core conda-forge/linux-64::jupyter_core-4.6.3-py38h32f6830_1
jupyterlab conda-forge/noarch::jupyterlab-2.2.4-py_0
jupyterlab_server conda-forge/noarch::jupyterlab_server-1.2.0-py_0
ld_impl_linux-64 conda-forge/linux-64::ld_impl_linux-64-2.34-hc38a660_9
libffi conda-forge/linux-64::libffi-3.2.1-he1b5a44_1007
libgcc-ng conda-forge/linux-64::libgcc-ng-9.3.0-h24d8f2e_14
libgomp conda-forge/linux-64::libgomp-9.3.0-h24d8f2e_14
libsodium conda-forge/linux-64::libsodium-1.0.18-h516909a_0
libstdcxx-ng conda-forge/linux-64::libstdcxx-ng-9.3.0-hdf63c60_14
libuuid conda-forge/linux-64::libuuid-2.32.1-h14c3975_1000
libuv conda-forge/linux-64::libuv-1.38.0-h516909a_0
markupsafe conda-forge/linux-64::markupsafe-1.1.1-py38h1e0a361_1
mistune conda-forge/linux-64::mistune-0.8.4-py38h1e0a361_1001
nbconvert conda-forge/linux-64::nbconvert-5.6.1-py38h32f6830_1
nbformat conda-forge/noarch::nbformat-5.0.7-py_0
ncurses conda-forge/linux-64::ncurses-6.2-he1b5a44_1
nodejs conda-forge/linux-64::nodejs-14.8.0-h568c755_0
notebook conda-forge/linux-64::notebook-6.1.1-py38h32f6830_0
openssl conda-forge/linux-64::openssl-1.1.1g-h516909a_1
packaging conda-forge/noarch::packaging-20.4-pyh9f0ad1d_0
pandoc conda-forge/linux-64::pandoc-2.10.1-h516909a_0
pandocfilters conda-forge/noarch::pandocfilters-1.4.2-py_1
parso conda-forge/noarch::parso-0.8.0-pyh9f0ad1d_0
pexpect conda-forge/linux-64::pexpect-4.8.0-py38h32f6830_1
pickleshare conda-forge/linux-64::pickleshare-0.7.5-py38h32f6830_1001
pip conda-forge/noarch::pip-20.2.2-py_0
prometheus_client conda-forge/noarch::prometheus_client-0.8.0-pyh9f0ad1d_0
prompt-toolkit conda-forge/noarch::prompt-toolkit-3.0.6-py_0
ptvsd conda-forge/linux-64::ptvsd-4.3.2-py38h516909a_1
ptyprocess conda-forge/noarch::ptyprocess-0.6.0-py_1001
pycparser conda-forge/noarch::pycparser-2.20-pyh9f0ad1d_2
pygments conda-forge/noarch::pygments-2.6.1-py_0
pyopenssl conda-forge/noarch::pyopenssl-19.1.0-py_1
pyparsing conda-forge/noarch::pyparsing-2.4.7-pyh9f0ad1d_0
pyrsistent conda-forge/linux-64::pyrsistent-0.16.0-py38h1e0a361_0
pysocks conda-forge/linux-64::pysocks-1.7.1-py38h32f6830_1
python conda-forge/linux-64::python-3.8.5-h4d41432_2_cpython
python-dateutil conda-forge/noarch::python-dateutil-2.8.1-py_0
python_abi conda-forge/linux-64::python_abi-3.8-1_cp38
pyzmq conda-forge/linux-64::pyzmq-19.0.2-py38ha71036d_0
readline conda-forge/linux-64::readline-8.0-he28a2e2_2
requests conda-forge/noarch::requests-2.24.0-pyh9f0ad1d_0
send2trash conda-forge/noarch::send2trash-1.5.0-py_0
setuptools conda-forge/linux-64::setuptools-49.3.1-py38h32f6830_0
six conda-forge/noarch::six-1.15.0-pyh9f0ad1d_0
sqlite conda-forge/linux-64::sqlite-3.32.3-hcee41ef_1
terminado conda-forge/linux-64::terminado-0.8.3-py38h32f6830_1
testpath conda-forge/noarch::testpath-0.4.4-py_0
tk conda-forge/linux-64::tk-8.6.10-hed695b0_0
tornado conda-forge/linux-64::tornado-6.0.4-py38h1e0a361_1
traitlets conda-forge/linux-64::traitlets-4.3.3-py38h32f6830_1
urllib3 conda-forge/noarch::urllib3-1.25.10-py_0
wcwidth conda-forge/noarch::wcwidth-0.2.5-pyh9f0ad1d_1
webencodings conda-forge/noarch::webencodings-0.5.1-py_1
wheel conda-forge/noarch::wheel-0.34.2-py_1
xeus conda-forge/linux-64::xeus-0.24.1-h4d8c418_0
xeus-python conda-forge/linux-64::xeus-python-0.8.0-py38hbf85e49_0
xz conda-forge/linux-64::xz-5.2.5-h516909a_1
zeromq conda-forge/linux-64::zeromq-4.3.2-he1b5a44_3
zipp conda-forge/noarch::zipp-3.1.0-py_0
zlib conda-forge/linux-64::zlib-1.2.11-h516909a_1007

```

And after I put "Yes" and all packages are installed. Terminal itself will tell me

![](assets/2020-08-13-02-31-59.png)

**And now I can see around 645MB of packages have been installed extra in `/home/paul/anaconda3/envs/jupyterlab-debugger`**
