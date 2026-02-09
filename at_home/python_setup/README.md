# Getting Set up with Python

Here, you will install Python on your local machine, which is the recommended approach. Nonetheless, if you prefer to use Python in a cloud-hosted environment instead, you can import the Jupyter Notebooks to [Google Colab](https://colab.research.google.com/) or [molab](https://molab.marimo.io/).

Note:

- If you already have Anaconda installed on your machine, it may not play nicely with VS Code by default unless you have added it to your system `PATH`, which the commands below achieve. If you want to use your pre-existing Anaconda environment, you need to provide the full path to the Python executable, which you can find via `which python` in the terminal.

## Installing Miniconda

### Windows

1. Download [Cmder (full)](https://cmder.app)
2. Extract the zip file and run `Cmder.exe`
3. Run the following in the Cmder terminal:

```bash
cd %USERPROFILE%
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S /AddToPath=1
del .\miniconda.exe
```

Notes:

- Please use Cmder and not PowerShell or the command prompt.
- Using Windows is fine in this course, but if you prefer, you can also install Linux on Windows [via WSL](https://learn.microsoft.com/en-us/windows/wsl/install).

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
uv pip install jupyter ipykernel ruff ase pymatgen
```

What we have done is made a dedicated environment for you to install all your Python packages in. It is better to use a dedicated environment rather than adding packaegs to your base environment because if something goes wrong, then you do not need to re-install Anaconda from scratch.

## Jupyter Notebook

If you do not already have VS Code installed on your computer, please install it as described [here](https://code.visualstudio.com/download) along with the following extensions: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), and [ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

Then you should try out the Jupyter Notebook, for instance by downloading and running [this test notebook](test.ipynb). Note that you will need to select your `cms` environment as the kernel in the Jupyter Notebook.

Note:

- If you are on Windows and trying to use the built-in terminal in VS Code, you will have a bad time. The easiest option is to simply use Cmder separately from VS Code. Alternatively, if you are feeling adventurous, you can try following the instructions [here](https://medium.com/talpor/windows-terminal-cmder-%EF%B8%8F-573e6890d143).
