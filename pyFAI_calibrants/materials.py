"""source information for the d-spacing calibration files to be created
from add new materials here; if the materials space group information is
not available add it to the file ./selection_rules.py
"""
from . import Material

al = Material(
    name="Al",
    space_group_number=225,
    a=4.04,
    b=4.04,
    c=4.04,
    alpha=90,
    beta=90,
    gamma=90,
    lattice="cubic",
    lattice_type="F",
)

au = Material(
    name="Au",
    space_group_number=225,
    a=4.17,
    b=4.17,
    c=4.17,
    alpha=90,
    beta=90,
    gamma=90,
    lattice="cubic",
    lattice_type="F",
)

cr = Material(
    name="Cr",
    space_group_number=229,
    a=2.87,
    b=2.87,
    c=2.87,
    alpha=90,
    beta=90,
    gamma=90,
    lattice="cubic",
    lattice_type="I",
)

graphite = Material(
    name="graphite",
    space_group_number=194,
    a=2.464,
    b=2.464,
    c=6.711,
    alpha=90,
    beta=90,
    gamma=120,
    lattice="hexagonal",
    lattice_type="P",
)

tise2 = Material(
    name="TiSe2",
    space_group_number=164,
    a=3.536,
    b=3.536,
    c=6.004,
    alpha=90,
    beta=90,
    gamma=120,
    lattice="trigonal",
    lattice_type="P",
)

vo2_monoclinic = Material(
    name="VO2_monoclinic",
    space_group_number=14,
    a=5.75,
    b=4.52,
    c=5.38,
    alpha=90,
    beta=122.6,
    gamma=90,
    lattice="monoclinic",
    lattice_type="P",
)

vo2_rutile = Material(
    name="VO2_rutile",
    space_group_number=136,
    a=4.55,
    b=4.55,
    c=2.86,
    alpha=90,
    beta=90,
    gamma=90,
    lattice="tetragonal",
    lattice_type="P",
)

tas2_trigonal = Material(
    name="TaS2_trigonal",
    space_group_number=164,
    a=3.38,
    b=3.38,
    c=6.17,
    alpha=90,
    beta=90,
    gamma=120,
    lattice="hexagonal",
    lattice_type="P",
)

znpc = Material(
    name="ZnPc",
    space_group_number=2,
    a=3.80520,
    b=12.95900,
    c=12.04300,
    alpha=90.6400,
    beta=95.2600,
    gamma=90.7200,
    lattice="monoclinic",
    lattice_type="P",
)