from ase.calculators.vasp import Vasp
from ase.io import read

atoms = read("Fe_hexagonal.cif")
atoms.set_initial_magnetic_moments([4.0] * len(atoms))
calc = Vasp(
    # Critical parameters
    xc="PBE",  # exchange-correlation functional ("level of theory"); sets GGA = PE here
    encut=520,  # plane-wave kinetic energy cutoff (convergence parameter)
    kspacing=0.4,  # k-point density (convergence parameter)
    ivdw=0,  # van der Waals corrections (0 = none, 12 = D3(BJ))
    # Important details
    isif=3,  # relaxation degrees of freedom (3 = relax positions+cell shape+cell volume)
    ediffg=-0.03,  # relaxation convergence criterion (eV/A)
    nsw=100,  # maximum number of relaxation steps
    # Additional parameters
    prec="accurate",  # high-precision calculations
    ediff=1e-5,  # SCF convergence criterion (eV)
    algo="fast",  # SCF convergence algorithm
    ibrion=2,  # relaxation algorithm (2 = conjugate-gradient)
    ismear=0,  # smearing method (0 = Gaussian smearing)
    sigma=0.05,  # smearing width (eV)
    lorbit=11,  # print out magnetic moments
    lasph=True,  # non-spherical corrections for 3d elements
    efermi="midgap",  # recommended by VASP
    gga_compat=False,  # recommended by VASP
)
atoms.calc = calc
atoms.get_potential_energy()
