from os.path import expanduser

# some globals
num_tests = 1
base_path = expanduser('~') + '/projects/injectionAnalysis/'
theo_fixed_r = base_path + 'theoretical_fixed_r/'
fixed_r = base_path + 'fixed_r_plots/'
fixed_domain = base_path + 'fixed_domain/'


# this should be a list of function names as strings
tests_to_run = [
        'theoretical_fixed_r'
        ]


# this should be a nested list of tuples of the parameters.
# functions are indexed by tests_to_run
test_params = [
        (1, 100, 100, 10000)
        ]

# min_r, max_r, num_tests, min_domain, max_domain
# fixed_domain, min codomain, max codomain, num tests

