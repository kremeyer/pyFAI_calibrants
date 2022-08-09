# pyFAI_calibrants
Collection of pyFAI calibration files

## installing the package
`python3 -m pip install git+https://github.com/kremeyer/pyFAI_calibrants`

## generating the d-spacing calibration files

`python3 -m pyFAI_calibrants`

The module will automatically generate d-spacing calibrations for all materials into the `calibrants` directory.

## adding new calibrants

To add a new calibrant, simply add the material information in to the `material.py` file. The space group is given as an integer. If no other material uses the space group of the new material, it's neccessary to add the selection rules.

```python3
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
```

## adding new selection rules

To add new selection rules of a space group, a new function in the file `selection_rules.py` needs to be created. The name should follow `__space_group_NNN` with `NNN` being the space group number with leading zeros. For example
```python3
def __space_group_229(h, k, l):
    if h == 0 and k == 0:
        return l % 2 == 0
    if h == 0 and l == 0:
        return k % 2 == 0
    if k == 0 and l == 0:
        return h % 2 == 0
    if k == l:
        return h % 2 == 0
    if h == l:
        return k % 2 == 0
    if h == k:
        return l % 2 == 0
    if l == 0:
        return (h + k) % 2 == 0
    if k == 0:
        return (h + l) % 2 == 0
    if h == 0:
        return (k + l) % 2 == 0
    return (h + k + l) % 2 == 0
```
