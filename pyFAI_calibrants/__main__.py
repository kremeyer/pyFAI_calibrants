from inspect import getmembers
from os import mkdir
from os.path import isdir, join
from pyFAI.calibrant import Cell
from . import materials, CALIB_DIR

if not isdir(CALIB_DIR):
    mkdir(CALIB_DIR)

for member in getmembers(materials):
    if isinstance(member[1], Cell):
        name = member[1].name
        member[1].save(name=member[1].name, dest_dir=CALIB_DIR, dmin=0.25)
