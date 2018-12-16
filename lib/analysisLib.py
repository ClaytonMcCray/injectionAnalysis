from lib.pyInjective import injective
from math import factorial

# in this file, k = size(domain), n = size(codomain)


# test returns the percent of tests run that were injective
# just a reminder -- pyInjective.injective will rasie RuntimeError
# if there's an issue from the CUDA port of the algortithm
def test(k, n, num_tests):
    inj_count = 0
    for i in range(num_tests):
        if injective(k, n):
            inj_count += 1

    return inj_count/num_tests * 100, inj_count


def num_injective(k, n):
    return factorial(n)//factorial(n-k)  # since n > n-k, it's safe to force integer division


def num_functions(k, n):
    return n ** k


def prob_injective(k, n, num_tests):
    inj = num_injective(k, n)
    num = num_functions(k, n)
    per = inj/num * 100
    expected = per/100 * num_tests
    return per, round(expected)


def percent_err(expected, actual):
    if actual != 0 and expected != 0:
        return abs(expected-actual)/actual * 100
    elif actual == 0 and expected != 0:
        return "ERROR"
    else:
        return 0
