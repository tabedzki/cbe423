# Getting Set up with Python

Here, you will install Python on your local machine, which is the recommended approach. Nonetheless, if you prefer to use Python in a cloud-hosted environment instead, I recommend using [molab](https://molab.marimo.io/).

## Installing Miniconda

### Windows

1. Download [Cmder (mini)](https://cmder.app)
2. Extract the zip file and run `Cmder.exe`
3. Run the following in the Cmder terminal:

```bash
cd %USERPROFILE%
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S /AddToPath=1
del .\miniconda.exe
```

Common issues:

- The commands do not necessarily work in PowerShell. Please use Cmder or the command prompt, although the former is preferred.

### Mac

Open the terminal and run the following commands:

If using Apple Silicon:

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
source ~/miniconda3/bin/activate
conda init --all
```

If using Apple Intel:

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
source ~/miniconda3/bin/activate
conda init --all
```

### Linux

Open the terminal and run the following commands:

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
source ~/miniconda3/bin/activate
conda init --all
```

## Making a Conda Environment

Restart the terminal and do the following to make a Conda environment named `cms` (cms = computational materials science):

```bash
conda create --name cms python=3.13
```

Make sure to accept the above terms of service. Then active your environment, install the packagage manager `uv`, and then use `uv` to install several Python packages in your `cms` environment:

```bash
conda activate cms
pip install uv
uv pip install jupyter ipykernel ruff
```

What we have done is made a dedicated environment for you to install all your Python packages in. It is better to use a dedicated environment rather than adding packaegs to your base environment because if something goes wrong, then you do not need to re-install Anaconda from scratch.

## Jupyter Notebook

If you do not already have VS Code installed on your computer, please install it as described [here](https://code.visualstudio.com/download) along with the following extensions: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), and [ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

Then you should try out the Jupyter Notebook, for instance by downloading and running [this example](https://github.com/Andrew-S-Rosen/cbe423/blob/main/lecture2/intro_pymatgen.ipynb). Note that you will need to select your `cms` environment as the kernel in the Jupyter Notebook.
