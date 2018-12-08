from ctypes import cdll
from sys import platform
from os import getcwd


if platform == "linux":
    lib = cdll.LoadLibrary(getcwd() + '/lib/bin/linux-gnu/injection.so')
elif platform == "darwin":
    lib = cdll.LoadLibrary(getcwd() + '/lib/bin/darwin17/injection.so')


class RandInjective(object):
    def __init__(self):
        self.obj = lib.randInjective_new()

    def injective(self, domain, codomain):
        return lib.randInjective_injective(self.obj, domain, codomain) == 1
