from os.path import expanduser

# some globals
num_tests = 1
base_path = expanduser('~') + '/projects/injectionAnalysis/'
theo_fixed_r = base_path + 'theoretical_fixed_r/'
fixed_r = base_path + 'fixed_r_plots/'
theo_fixed_domain = base_path + 'theoretical_fixed_domain/'
fixed_domain = base_path + 'fixed_domain/'


# this should be a list of function names as strings
tests_to_run = [
        'fixed_r_plots'
        ]


# this should be a nested list of tuples of the parameters.
# functions are indexed by tests_to_run
test_params = [
        (10, 10, 10, 1000, 25, 10)
        ]

# Function headers #####################################################
# fixed_domain_plots(domain, min_codomain, max_codomain, num_tests, codomain_skip=5)
# theoretical_fixed_domain(domain, min_codomain, max_codomain, codomain_skip=5)
# fixed_r_plots(min_r, max_r, min_domain, max_domain, num_tests, domain_skip=5)
# theoretical_fixed_r(min_r, max_r, min_domain, max_domain, domain_skip=5)
#########################################################################

# min_r, max_r, num_tests, min_domain, max_domain
# fixed_domain, min codomain, max codomain, num tests

