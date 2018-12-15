#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd

from load_datas import load_datas, courses
from parsing import parse_main

def trim_name(e):
	return e if len(e) <= 8 else e[0:6] + '..'

if __name__ == '__main__':
	args = parse_main()
	d = load_datas(args.filename)

	font = { 'size': 8 }
	matplotlib.rc('font', **font)

	#TODO: colors ?
	#TODO: title
	d.columns = [trim_name(e) for e in courses]
	axes = pd.plotting.scatter_matrix(d, figsize=(16, 12))
	for a in axes.flatten():
		a.set_yticklabels([])
		a.set_xticklabels([])
	
	plt.show()