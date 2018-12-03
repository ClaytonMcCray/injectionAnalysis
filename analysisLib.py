from pyInjective import rand_injective
from math import factorial

# in this file, k = size(domain), n = size(codomain)
p = rand_injective()


# test returns the percent of tests run that were injective
def test(k, n, num_tests):
    inj_count = 0
    for i in range(num_tests):
        if p.injective(k, n):
            inj_count += 1

    return inj_count/num_tests * 100


def num_injective(k, n):
    return factorial(n)//factorial(n-k)  # since n > n-k, it's safe to force integer division


def num_functions(k, n):
    return n ** k


def prob_injective(k, n):
    return num_injective(k, n)/num_functions(k, n) * 100
