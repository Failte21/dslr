#! /usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

from load_datas import load_datas, courses
from parsing import parse_main

if __name__ == '__main__':

    #TODO: colors
    #TODO: legend

    args = parse_main()
    d = load_datas(args.filename, ['Hogwarts House'])
    gryffindor = d[(d['Hogwarts House'] == 'Gryffindor')].drop(['Hogwarts House'], axis=1)
    hufflepuff = d[(d['Hogwarts House'] == 'Hufflepuff')].drop(['Hogwarts House'], axis=1)
    slytherin = d[(d['Hogwarts House'] == 'Slytherin')].drop(['Hogwarts House'], axis=1)
    ravenclaw = d[(d['Hogwarts House'] == 'Ravenclaw')].drop(['Hogwarts House'], axis=1)

    fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(16, 12))
    for i, c in enumerate(courses):
        df = pd.concat([
            gryffindor[c],
            hufflepuff[c],
            slytherin[c],
            ravenclaw[c],
        ], axis=1, keys=['gryffindor', 'hufflepuff', 'slytherin', 'ravenclaw'])
        x = i % 4
        y = int(i / 4)
        a = df.plot.hist(stacked=True, bins=20, ax=axes[y,x], legend=False)
        a.set_ylabel(c)
    plt.show()