# some globals
num_tests = 1


# this should be a list of function names as strings
tests_to_run = [
        'fixed_r_plots',
        'fixed_domain_plots'
        ]


# this should be a nested list of tuples of the parameters.
# functions are indexed by tests_to_run
test_params = [
        (1, 2, num_tests, 1, 10),
        (100, 100, 1000, num_tests)
        ]

# min_r, max_r, num_tests, min_domain, max_domain
# fixed_domain, min codomain, max codomain, num tests

