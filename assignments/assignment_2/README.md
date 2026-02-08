# Slurm Usage

For this assignment, you will run calculations on the Adroit test cluster. As a reminder, to log into the Adroit test cluster, you can either use http://myadroit.princeton.edu (must be on the Princeton network or VPN) or ssh `<NetID>@adroit.princeton.edu` from the command line.

You should run your calculations in `/scratch/network/<NetID>` rather than your home directory, as the latter is not meant for fast I/O operations. Remember that you can use cd `/path/to/directory` to change directories.

To submit jobs to the queue, you will need to use one of the `submit.job` files that we provide on Canvas. The jobs can be submitted to the Slurm queue via sbatch submit.job. Princeton Research Computing has substantial documentation on how to use Slurm if needed, but the main commands you need to know are: `squeue --me` (show all your jobs) and `scancel <JobID>` (cancel a job). A job in state `Q` means it is queued and `R` means running. After you submit a job, a `slurm-######.out` file will be written, which can contain useful information (e.g. warning or error messages) if you make a mistake.

# VASP

Once a VASP calculation starts, the main information will be stored in the `OUTCAR`, and the phrase "reached required accuracy" will appear near the bottom if successful. Once the calculation is complete, the final structure can be found in the `CONTCAR` file, which you should view in VESTA or ASE.

To get information about the energy, forces, and other properties, you can read the `OUTCAR` as follows:

```python
from ase.io import read

list_atoms = read("OUTCAR", index=":")
final_atoms = list_atoms[-1]
e = final_atoms.get_potential_energy()
print(e)
```

Additionally, on your local machine you can see a plot of the optimization trajectory with `ase gui OUTCAR` in the command-line.

Additional details about VASP can be found below:

- https://vasp.at/wiki/The_VASP_Manual
- https://www.vasp.at/documentation/

# ORCA

The main output information can be found in `orca.out`. You will see "ORCA TERMINATED NORMALLY" for a successful calculation. The 0 K total energy can be found under the "FINAL SINGLE POINT ENERGY" section. Vibrational frequencies, if calculated, can be found under the "VIBRATIONAL FREQUENCIES" section, and thermochemical properties can be found at the "THERMOCHEMISTRY" section.

Additional details about ORCA can be found below:

- https://www.faccts.de/docs/orca/6.1/manual/
- https://www.faccts.de/docs/orca/6.1/tutorials/index.html
