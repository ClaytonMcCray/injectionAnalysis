from analysisLib import *


def print_data(data):
    labels = ["Domain Size: ", "Codomain Size: ", "Number of Tests Run: ", "Ratio Codomain/Domain: ",
              "Actual Percent Injective: ", "Actual Injective: ", "Expected Percent Injective: ",
              "Expected Injective: ", "Percent Error: "]

    for i in range(len(data)):
        print(labels[i], data[i], " ", end='')

    print()


def main():
    r = 3  # the ratio codomain/domain
    data = []
    num_tests = 10000
    for domain in range(1000):
        actual_per, actual_count = test(domain, r*domain, num_tests)
        expected, expected_count = prob_injective(domain, r*domain, num_tests)
        error = percent_err(expected, actual_per)
        data = [domain, r*domain, num_tests, r, actual_per, actual_count, expected, expected_count, error]
        print_data(data)


main()
