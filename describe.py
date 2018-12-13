#! /usr/bin/env python3

import numpy as np
import sys
import math

from ft_libml import *
from errors import exit_usage
from load_datas import load_datas

#TODO: convert to class

def trim_name(e):
    l_max = 15
    return e if len(e) <= l_max else e[0:l_max - 3] + '...'

def print_header(h_part, sm_pad, lg_pad):
    h_part_space = [''] + h_part

    for i, h in enumerate(h_part_space):
        pad = lg_pad if i > 0 else sm_pad
        endchar = '' if i + 1 < len(h_part_space) else '\n'
        print(f'{h:>{pad}}', end=endchar)

def print_datas(h_part, sm_pad, lg_pad, fns, s):
    for l in fns:
        print(f'{l:<{sm_pad}}', end='')
        for i in range(s, s + len(h_part)):
            curr = d[:,i]
            v = fns[l](curr)
            print(f'{int(v):>{lg_pad}}', end='')
        print('')

def ft_describe(d, headers):
    sm_pad = 8
    lg_pad = 17
    feat_per_row = 7
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

    for j in range(math.ceil(nb_features / feat_per_row)):
        s = j * feat_per_row
        e = s + feat_per_row
        h_part = [trim_name(e) for e in headers[s:e]]

        print_header(h_part, sm_pad, lg_pad)
        print_datas(h_part, sm_pad, lg_pad, fns, s)
        print('')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit_usage()
    d, headers = load_datas(sys.argv[1])
    ft_describe(d, headers)