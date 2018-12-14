#! /usr/bin/env python3

import sys
import pandas as pd
import ft_libml as lml

from errors import exit_usage
from load_datas import load_datas

def ft_describe(d):
    df = d.agg([
        lml.count,
        lml.mean,
        lml.std,
        lml.min,
        lml.per_25,
        lml.per_50,
        lml.per_75,
        lml.max
    ]).rename({
        'per_25': '25%',
        'per_50': '50%',
        'per_75': '75%',
    }, axis='index')
    print(df)

    #DEBUG
    # print('')
    # print(d['Arithmancy'].count())
    # print(d['Arithmancy'].mean())
    # print(d['Arithmancy'].std())
    # print(d['Arithmancy'].min())
    # print(d['Arithmancy'].max())
    # print(d['Arithmancy'].quantile(.25))
    # print(d['Arithmancy'].quantile(.5))
    # print(d['Arithmancy'].quantile(.75))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit_usage()
    d = load_datas(sys.argv[1])
    ft_describe(d)
