#! /usr/bin/env python3

import math
import numpy as np
import pandas as pd

from load_datas import load_datas, courses
from parsing import parse_main

def sigmoid(x):
    return 1 / (1 + math.exp(x))

#TODO: scope that
vsigmoid = np.vectorize(sigmoid)

def hypothesis(t, x):
	return (vsigmoid(np.transpose(t) * x))

if __name__ == '__main__':
	args = parse_main()
	df = load_datas(args.filename, ['Hogwarts House'])

	houses = ['Gryffindor', 'Hufflepuff', 'Slytherin', 'Ravenclaw']
	X = df[courses].values
	m, n = X.shape
	thetas = pd.DataFrame(0, index=np.arange(n), columns=(houses))

	for house in houses:
		t = thetas[house].values
		h = hypothesis(t, X)
		y = df['Hogwarts House'].apply(lambda x: 1 if x == house else 0).values
	