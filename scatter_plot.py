#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib

from load_datas import load_datas, courses
from parsing import parse_main

def trim_name(e):
	return e if len(e) <= 8 else e[0:6] + '..'

if __name__ == '__main__':
	args = parse_main()
	d = load_datas(args.filename)

	font = { 'size': 8 }
	matplotlib.rc('font', **font)

	fig, axes = plt.subplots(nrows=13, ncols=13, figsize=(16, 12))
	for y in range(13):
		for x in range(y,13):
			d.plot.scatter(courses[x], courses[y], ax=axes[x,y])

	plt.show()