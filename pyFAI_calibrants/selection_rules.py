"""the selection rules for the scattering for each space group can be
found at http://img.chem.ucl.ac.uk/sgp/LARGE/SGP.HTM
"""
from inspect import getmembers
import sys


def get_selection_rules(space_group_number):
    func_name = f"__space_group_{space_group_number:03d}"
    memberlist = getmembers(sys.modules[__name__])
    memberdict = dict(memberlist)

    if func_name in memberdict.keys():
        return memberdict[func_name]

    raise ValueError(
        f"the selection rules for space group {space_group_number} have not been implemented, yet"
    )


def __space_group_014(h, k, l):
    if h == k:
        return l % 2 == 0
    if h == 0 and l == 0:
        return k % 2 == 0
    if k == 0:
        return l % 2 == 0
    return True


def __space_group_136(h, k, l):
    if h == 0 and k == 0:
        return l % 2 == 0
    if h == 0 and l == 0:
        return k % 2 == 0
    if k == 0 and l == 0:
        return h % 2 == 0
    if k == l:
        return h % 2 == 0
    if k == 0:
        return (h + l) % 2 == 0
    if h == 0:
        return (k + l) % 2 == 0
    return True


def __space_group_164(h, k, l):
    return True


def __space_group_194(h, k, l):
    if h == k:
        return l % 2 == 0
    if h == 0 and k == 0:
        return l % 2 == 0
	return True


def __space_group_225(h, k, l):
    if h == k and l == 0:
        return h % 2 == 0
    if h == l and k == 0:
        return h % 2 == 0
    if k == l and h == 0:
        return k % 2 == 0
    if h == 0 and k == 0:
        return l % 2 == 0
    if h == 0 and l == 0:
        return k % 2 == 0
    if k == 0 and l == 0:
        return k % 2 == 0
    if k == l:
        return (h + k) % 2 == 0
    if h == l:
        return (h + k) % 2 == 0
    if h == k:
        return (h + l) % 2 == 0
    if l == 0:
        return h % 2 == 0 and k % 2 == 0
    if k == 0:
        return h % 2 == 0 and l % 2 == 0
    if h == 0:
        return k % 2 == 0 and l % 2 == 0
    return (h + k) % 2 == 0 and (h + l) % 2 == 0 and (k + l) % 2 == 0


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
