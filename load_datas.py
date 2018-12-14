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