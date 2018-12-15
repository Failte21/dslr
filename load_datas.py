from errors import exit_usage
import numpy as np
import pandas as pd

courses = ["Arithmancy",
    "Astronomy",
    "Herbology",
    "Defense Against the Dark Arts",
    "Divination",
    "Muggle Studies",
    "Ancient Runes",
    "History of Magic",
    "Transfiguration",
    "Potions",
    "Care of Magical Creatures",
    "Charms",
    "Flying"
]

def load_datas(filename, extra=[]):
    try:
        d = pd.read_csv(filename, usecols=courses + extra)
        return d
    except ValueError:
        exit_failure(f'Can\'t load file {filename}')

def filter_houses(d):
	gryffindor = d[(d['Hogwarts House'] == 'Gryffindor')].drop(['Hogwarts House'], axis=1)
	hufflepuff = d[(d['Hogwarts House'] == 'Hufflepuff')].drop(['Hogwarts House'], axis=1)
	slytherin = d[(d['Hogwarts House'] == 'Slytherin')].drop(['Hogwarts House'], axis=1)
	ravenclaw = d[(d['Hogwarts House'] == 'Ravenclaw')].drop(['Hogwarts House'], axis=1)
	return [gryffindor, hufflepuff, slytherin, ravenclaw]