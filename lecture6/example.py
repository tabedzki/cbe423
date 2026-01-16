from ase.build import bulk
from ase.calculators.vasp import Vasp

atoms = bulk("Cu")

# This is a minimal example and very inaccurate!
# In practice, you would need to set many more VASP parameters.
# Again, this is not a "real" calculation!
atoms.calc = Vasp(xc="PBE")
atoms.get_potential_energy()
