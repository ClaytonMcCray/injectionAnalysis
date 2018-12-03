from pyInjective import rand_injective

p = rand_injective()
domain = 100
codomain = 100
num_tests = 1000


def test(dom_mult, co_mult):
    inj_count = 0
    for i in range(num_tests):
        if p.injective(domain * dom_mult, codomain * co_mult):
            inj_count += 1

    return inj_count


for i in range(100):
    print("Multipliers 2 :", i, " -- ", test(2, i) / num_tests * 100, "% of tests were injective")

