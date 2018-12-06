#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    data = np.loadtxt("resources/dataset_train.csv", dtype='str', delimiter=',')
    classes = ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 
        'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic',
        'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying'
    ]

    gryffindor = data[data[:,1] == 'Gryffindor']
    hufflepuff = data[data[:,1] == 'Hufflepuff']
    slytherin = data[data[:,1] == 'Slytherin']
    ravenclaw = data[data[:,1] == 'Ravenclaw']
    fig, axes = plt.subplots(nrows=3, ncols=4)
    colors = ['red', 'tan', 'lime', 'blue']
    n_bins = 10
    for i in range(6,18):
        g = [float(e) for e in gryffindor[:,i] if e != '']
        h = [float(e) for e in hufflepuff[:,i] if e != '']
        s = [float(e) for e in slytherin[:,i] if e != '']
        r = [float(e) for e in ravenclaw[:,i] if e != '']
        x = np.array([g, h, s, r])
        axes.flatten()[i - 6].hist(x, n_bins, histtype='bar')

    plt.show()