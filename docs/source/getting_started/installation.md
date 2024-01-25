# Installation

|OS|Linux|Windows|Mac|
|:-:|:-:|:-:|:-:|
|**compatibility**|Yes|Yes|Yes| 

## Install conda

*We use conda environment to avoid version problem between pyHiM dependencies and other applications.*

You can choose between the lighter version `miniconda` or the full `anaconda` which comes with the spyder IDE.

- [Installing conda on Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)
- [Installing conda on Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)
- [Installing conda on macOS](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)

## Create conda environment

Open a **terminal** (for Windows user: from the Start menu, open the **Anaconda Prompt**). Create a conda environment and activate it:
```
conda create -n apiFISH-env python=3.9
conda activate apiFISH-env
```

## Install apiFISH

```bash
pip install apifish
```

