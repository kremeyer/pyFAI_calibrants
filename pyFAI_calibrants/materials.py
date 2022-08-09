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

vo2_monoclinic = Material(
    name="VO2_monoclinic",
    space_group_number=14,
    a=5.48,
    b=5.15,
    c=9.22,
    alpha=90,
    beta=90.58,
    gamma=90,
    lattice="monoclinic",
    lattice_type="P",
)

vo2_rutile = Material(
    name="VO2_rutile",
    space_group_number=136,
    a=4.52,
    b=4.52,
    c=3.04,
    alpha=90,
    beta=90,
    gamma=90,
    lattice="tetragonal",
    lattice_type="P",
)
