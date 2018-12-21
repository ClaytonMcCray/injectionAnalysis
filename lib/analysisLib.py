from lib.pyInjective import injective
from math import factorial

# in this file, k = size(domain), n = size(codomain)


# test returns the percent of tests run that were injective
# just a reminder -- pyInjective.injective will rasie RuntimeError
# if there's an issue from the CUDA port of the algortithm
def test(d, c, num_tests):
    inj_count = 0
    for i in range(num_tests):
        if injective(d, c):
            inj_count += 1

    return inj_count/num_tests * 100, inj_count


def num_injective(d, c):
    return factorial(c)//factorial(c-d)  # since n > n-k, it's safe to force integer division


def num_functions(d, c):
    return c ** d


# techinically this is correct and I think it's the clearer form, so I'm leaving it
def theoretical_prob_injective_slow(d, c):
    return 100 * num_injective(d, c) / num_functions(d, c)


# this is a more optimized version of the slow above
def theoretical_prob_injective(d, c):
    i = 1
    for j in range(c-d+1, c+1):
        i *= j
    return 100 * (i / num_functions(d, c))


def prob_injective(d, c, num_tests):
    inj = num_injective(d, c)
    num = num_functions(d, c)
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
