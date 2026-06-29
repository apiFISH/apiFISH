# How to run a notebook

*A jupyter notebook is an interactive file where you can find both markdown text and executable code with its outputs displayed.*

*The main apiFISH tutorials is in this format.*

## Install and configure JupyterLab

1. Activate your [conda environment](../quick_install.md#create-conda-environment) for pyHiM:

```sh
conda activate apiFISH-env
```


```{note}
Replace `apiFISH-env` by your `environment name` if you called it something else.
```

2. Install a tool to manage jupyter notebook like [JupyterLab: <img src="notebooks/_static/Download-Icon.png" width="50"/>](https://jupyter.org/install#jupyterlab)
```sh
conda install jupyterlab
```

3. We recommend to create a specific kernel to run on JupyterLab with the good environment:

```
conda install ipykernel
ipython kernel install --user --name=apiFISH-kernel
```

## Open tutorial with JupyterLab

1. Download and unzip your notebook tutorial
<!-- , [click here: <img src="notebooks/_static/Download-Icon.png" width="50"/>](links to tuto) -->

2. Open a terminal inside your downloaded folder and activate your [conda environment](../quick_install.md#create-conda-environment) for apiFISH:
```sh
conda activate apiFISH-env
```

3. Open your tutorial with JupiterLab (or jupyter notebook):
```sh
jupyter-lab <tutorial_name>.ipynb
```

4. Once you spin up a jupyter lab from the `apiFISH-env` environment, select the `apiFISH-kernel` (click on panel Kernel > Change Kernel...) to be able to run *apiFISH* functions.

![select_kernel_screenshot](../../_static/select_kernel.png)

5. Now you can follow the tutorial by running each cell with the `run` icon (or `Shift+Enter` on keyboard):

![run_notebook_screenshot](../../_static/run_notebook.png)