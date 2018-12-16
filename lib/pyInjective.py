from ctypes import CDLL
from sys import platform
from os import getcwd


if platform == "linux":
    lib = CDLL(getcwd() + '/lib/bin/linux-gnu/injection.so')
elif platform == "darwin":
    lib = CDLL(getcwd() + '/lib/bin/darwin17/injection.so')


def injective(domain, codomain):
    ret_val = lib.injective(domain, codomain)
    if ret_val == 1:
        return True
    elif ret_val == 0:
        return False
    else:
        raise RuntimeError

