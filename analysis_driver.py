from lib.analysisLib import *
import csv
import matplotlib.pyplot as plt
from os.path import expanduser, isdir
from os import mkdir
from datetime import datetime
import config


# TODO #####################
#   * Need to make a test config. Will be config.py
#     to replace the garbage below cluttering up the driver.



def fixed_domain_plots(domain, min_codomain, max_codomain, num_tests):
    per_dat_points = []
    co_dat_points = []
    codomain = min_codomain
    while codomain <= max_codomain:
        actual_per, _ = test(domain, codomain, num_tests)
        per_dat_points.append(actual_per)
        co_dat_points.append(codomain)
        codomain += 1

    plt.scatter(co_dat_points, per_dat_points)
    plt.title("Fixed Domain Plot, k = " + str(domain) + ", Number of Tests: " + str(num_tests))
    plt.xlabel("Codomain Size")
    plt.ylabel("% Actual Injective")

    savepath = expanduser('~') + '/projects/injectionAnalysis/fixed_domain_plots/' + str(datetime.now()) + '/'
    if not isdir(savepath):
        mkdir(savepath)

    plt.savefig(savepath + "d" + str(domain) + "tests" + str(num_tests) + ".png")
    plt.clf()


def fixed_r_plots(min_r, max_r, num_tests, min_domain, max_domain):
    r = min_r
    savepath = expanduser('~') + '/projects/injectionAnalysis/fixed_r_plots/' + str(datetime.now()) + '/'
    if not isdir(savepath):
        mkdir(savepath)

    while r <= max_r:  # the ratio codomain/domain
        domain = min_domain
        per_dat_points = []
        dom_dat_points = []
        while domain <= max_domain:
            actual_per, actual_count = test(domain, r*domain, num_tests)

            # data points
            per_dat_points.append(actual_per)
            dom_dat_points.append(domain)

            domain += 1

        plt.scatter(dom_dat_points, per_dat_points)
        plt.title("Fixed r Plot, r = " + str(r) + ", Number of Tests: " + str(num_tests))
        plt.xlabel("Domain Size")
        plt.ylabel("% Actual Injective")
        plt.savefig(savepath + "r" + str(r) + "tests" + str(num_tests) + ".png")
        plt.clf()
        r += 1



# func = name of function to call from config.py
# idx = index of function -> parameters
for idx, func in enumerate(config.tests_to_run):
    globals()[func](*config.test_params[idx])


