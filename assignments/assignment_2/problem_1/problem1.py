from ase.calculators.vasp import Vasp
from ase.io import read

atoms = read("</path/to/structure.cif>")
atoms.calc = Vasp(
    # Level of Theory:
    xc="<Functional>",  # Exchange-correlation functional
    ivdw=<Integer>,  # van der Waals corrections (0 = none; 12 = D3(BJ))
    # Convergence parameters:
    encut=650,  # Energy cutoff in eV (higher for more accuracy)
    kspacing=0.4,  # k-point spacing in 1/Angstrom (lower for dense grid)
    # Relaxation parameters:
    isif=<Integer>,  # Relax ions and cell shape/volume (2 = ions only; 3 = ions + cell)
    ibrion=2,  # Ionic relaxation algorithm (2 = conjugate gradient)
    ediffg=-0.02,  # |ediffg| is the max|F| in eV/A for relaxation to convegrge
    nsw=200,  # Maximum number of ionic steps
    # Electronic parameters:
    prec="accurate",  # Precision mode
    ediff=1e-5,  # SCF convergence tolerance in eV
    algo="all",  # SCF convergence algorithm
    ismear=0,  # Gaussian smearing for insulators
    sigma=0.01,  # Fermi smearing width in eV
    # Niche parameters:
    lorbit=11,  # Write out magnetic moments if applicable
    lasph=True,  # VASP recommends this for greater accuracy
    gga_compat=False,  # VASP recommends this for greater accuracy
)
initial_magmoms = [<Value>] * len(atoms)  # Initial guess for magnetic moments
atoms.set_initial_magnetic_moments(initial_magmoms)
atoms.get_potential_energy()  # Runs the calculation
