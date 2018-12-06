#! /usr/bin/env python3

import numpy as np
import pandas as pd
import sys

from ft_libml import *

def exit_failure(msg):
    print(msg)
    sys.exit()

def exit_usage():
    exit_failure("Usage: describe.py [csv file name]")

def to_float(a):
    try:
        float(a)
        return True
    except:
        return False

def load_datas(filename):
    try:
        d = np.genfromtxt(filename, skip_header=1, filling_values=-999, delimiter=',')
        return d[:,d[0,:] != -999]
    except ValueError:
        exit_failure(f'Can\'t load file {filename}')

def ft_describe(d):
    labels = ["Count","Mean","Std","Min","25%","50%","75%","Max"]
    fns = {
        "Count": ft_count,
        "Mean": ft_mean,
        "Std": ft_std,
        "Min": ft_min,
        "25%": ft_mean,
        "50%": ft_mean,
        "75%": ft_mean,
        "Max": ft_max
    }
    values = []
    nb_features = len(d[0,:])

    # Header
    print('\t', end='')
    for i in range(nb_features):
        endchar = '\t' if i + 1 < nb_features else '\n'
        print(f'Feat{i}', end=endchar)

    for l in labels:
        print(l, end='\t')
        for i in range(nb_features):
            curr = d[:,i]
            v = fns[l](curr)
            print(int(v), end='\t')
        print('\n')

if __name__ == '__main__':
    # print(ft_min([1,2,-5]))
    # sys.exit()
    if len(sys.argv) != 2:
        exit_usage()
    # v = np.vectorize(to_float)
    d = load_datas(sys.argv[1])
    ft_describe(d)
    s = pd.Series(d[:,0])
    print(s.describe())