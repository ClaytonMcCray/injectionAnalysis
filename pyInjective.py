from ctypes import cdll
from sys import platform

os_type = platform


if platform == "linux":
    lib = cdll.LoadLibrary('./linux-gnu/injection.so')


class rand_injective(object):
    def __init__(self):
        self.obj = lib.randInjective_new()

    def injective(self, domain, codomain):
        return lib.randInjective_injective(self.obj, domain, codomain) == 1
