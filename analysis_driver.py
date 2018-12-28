from lib.analysisLib import *
import csv
import matplotlib.pyplot as plt
from os.path import isdir
from os import mkdir
from datetime import datetime
import config


# TODO #####################
#   * Need to make a test config. Will be config.py
#     to replace the garbage below cluttering up the driver.



def fixed_domain_plots(domain, min_codomain, max_codomain, num_tests, codomain_skip=5):
    per_dat_points = []
    co_dat_points = []
    codomain = min_codomain
    for codomain in range(min_codomain, max_codomain + 1, codomain_skip):
        actual_per, _ = test(domain, codomain, num_tests)
        per_dat_points.append(actual_per)
        co_dat_points.append(codomain)

    plt.ylim(0, 105)
    plt.scatter(co_dat_points, per_dat_points)
    plt.title("Fixed Domain Plot, k = " + str(domain) + ", Number of Tests: " + str(num_tests))
    plt.xlabel("Codomain Size")
    plt.ylabel("% Actual Injective")

    savepath = config.fixed_domain + str(datetime.now()) + '/'
    if not isdir(config.fixed_domain):
        mkdir(config.fixed_domain)
    if not isdir(savepath):
        mkdir(savepath)

    plt.savefig(savepath + "d" + str(domain) + "tests" + str(num_tests) + ".png")
    plt.clf()


def theoretical_fixed_domain(min_domain, max_domain, min_codomain, max_codomain, codomain_skip=5):
    # build directory
    if not isdir(config.theo_fixed_domain):
        mkdir(config.theo_fixed_domain)
    savepath = config.theo_fixed_domain + str(datetime.now()) + '/'
    if not isdir(savepath):
        mkdir(savepath)
    
    for domain in range(min_domain, max_domain + 1):
        # it doesn't make sense to look at data for which the following is untrue
        if domain < min_codomain:
            pass
        per_dat_points = []
        co_dat_points = []
        for codomain in range(min_codomain, max_codomain + 1, codomain_skip):
            per_dat_points.append(theoretical_prob_injective(domain, codomain))
            co_dat_points.append(codomain)

        plt.ylim(0, 105)
        plt.scatter(co_dat_points, per_dat_points)
        plt.title('Theoretical Fixed Domain Plot, d = ' + str(domain))
        plt.xlabel('Codomain Size')
        plt.ylabel('Probability of Injectiveness')
        plt.savefig(savepath + 'd' + str(domain) + '.png')
        plt.clf()


def fixed_r_plots(min_r, max_r, min_domain, max_domain, num_tests, domain_skip=5):
    savepath = config.fixed_r + str(datetime.now()) + '/'
    if not isdir(config.fixed_r):
        mkdir(config.fixed_r)
    if not isdir(savepath):
        mkdir(savepath)

    for r in range(min_r, max_r + 1):  # the ratio codomain/domain
        per_dat_points = []
        dom_dat_points = []
        for domain in range(min_domain, max_domain + 1, domain_skip):
            actual_per, actual_count = test(domain, r*domain, num_tests)

            # data points
            per_dat_points.append(actual_per)
            dom_dat_points.append(domain)

        plt.ylim(0, 105)
        plt.scatter(dom_dat_points, per_dat_points)
        plt.title("Fixed r Plot, r = " + str(r) + ", Number of Tests: " + str(num_tests))
        plt.xlabel("Domain Size")
        plt.ylabel("% Actual Injective")
        plt.savefig(savepath + "r" + str(r) + "tests" + str(num_tests) + ".png")
        plt.clf()


def theoretical_fixed_r(min_r, max_r, min_domain, max_domain, domain_skip=5):
    r = min_r
    if not isdir(config.theo_fixed_r):
        mkdir(config.theo_fixed_r)
    savepath = config.theo_fixed_r + str(datetime.now()) + '/'
    if not isdir(savepath):
        mkdir(savepath)

    for r in range(min_r, max_r + 1):
        per_dat_points = []
        dom_dat_points = []
        for domain in range(min_domain, max_domain + 1, domain_skip):
            per_dat_points.append(theoretical_prob_injective(domain, r*domain))
            dom_dat_points.append(domain)

        plt.ylim(0, 105)
        plt.scatter(dom_dat_points, per_dat_points)
        plt.title("Theoretical Fixed r Plot, r = " + str(r))
        plt.xlabel("Domain Size")
        plt.ylabel("Probabilty of Injectiveness")
        plt.savefig(savepath + "r" + str(r) + ".png")
        plt.clf()




# Reading in the config and running tests #########################################
# func = name of function to call from config.py
# idx = index of function -> parameters
for idx, func in enumerate(config.tests_to_run):
    globals()[func](*config.test_params[idx])
    print(idx, func)


