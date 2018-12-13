from errors import exit_usage
import numpy as np

def load_datas(filename):
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

    try:
        d = np.genfromtxt(filename,
         filling_values=0, #TODO: might create problems
         delimiter=',',
         usecols=(6,7,8,9,10,11,12,13,14,15,16,17,18)
    )
        return (d, courses) #TODO: get name from data (not hardcoded)
    except ValueError:
        exit_failure(f'Can\'t load file {filename}')