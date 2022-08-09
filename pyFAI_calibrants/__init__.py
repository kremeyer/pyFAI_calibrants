from pyFAI.calibrant import Cell
from .selection_rules import get_selection_rules

VERSION = 0.1
CALIB_DIR = "calibrants"


class Material(Cell):
    def __init__(self, name, space_group_number, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)
        self.selection_rules.append(get_selection_rules(space_group_number))

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f"saved calibrant to {kwargs['dest_dir']}/{kwargs['name']}.D")
