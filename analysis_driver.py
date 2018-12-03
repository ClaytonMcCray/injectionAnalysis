from analysisLib import *


num_tests = 100

for dom in range(100):
    for co in range(1000):
        if dom < co:
            print("(", dom, ",", co, ") Actual: ", test(dom, co, num_tests), "Expected: ", prob_injective(dom, co))

