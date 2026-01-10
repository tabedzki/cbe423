# Getting Set up with Python

## Installing Miniconda

### Windows

1. If you do not have a terminal client, download [Cmder (mini)](https://cmder.app)
2. Extract the zip file and run `cmder.exe`
3. Run the following in the Cmder terminal:

```bash
cd %USERPROFILE%
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S /AddToPath=1
del .\miniconda.exe
```

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
