#! /usr/bin/env python3

import os
import numpy as np
import pandas as pd
import sys

from ft_libml import *

def exit_failure(msg):
    print(msg)
    sys.exit()

def exit_usage():
    exit_failure("Usage: describe.py [csv file name]")

def load_datas(filename):
    try:
        d = np.genfromtxt(filename, skip_header=1, filling_values=-999, delimiter=',')
        return d[:,d[0,:] != -999]
    except ValueError:
        exit_failure(f'Can\'t load file {filename}')

def ft_describe(d, n):
    sm_pad = 5
    lg_pad = 15

    fns = {
        "Count": ft_count,
        "Mean": ft_mean,
        "Std": ft_std,
        "Min": ft_min,
        "25%": ft_percentile(25),
        "50%": ft_mean,
        "75%": ft_percentile(75),
        "Max": ft_max
    }
    values = []

    # Header
    for i in range(n + 1):
        pad = lg_pad if i > 0 else sm_pad
        e = f'Feature{i}' if i > 0 else ''
        endc = '\n' if i == n else '' 
        print(f'{e:>{pad}}', end=endc)

    for l in fns:
        print(f'{l:<{sm_pad}}', end='')
        for i in range(n):
            curr = d[:,i]
            v = f'{fns[l](curr):.6f}'
            print(f'{v:>{lg_pad}}', end='')
        print('')

if __name__ == '__main__':
    # rows, columns = os.popen('stty size', 'r').read().split() //TODO : maybe fancy print
    
    if len(sys.argv) != 2:
        exit_usage()
    d = load_datas(sys.argv[1])
    n = len(d[0,:])

    ft_describe(d, n)

    #PANDA print to compare
    # datadict = {}
    # for i in range(n):
    #     key = f'Feature{i + 1}'
    #     datadict[key] = d[:,i]
    # s = pd.DataFrame(datadict)
    # print(s.describe())