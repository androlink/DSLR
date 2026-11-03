from matplotlib.axes import Axes
import stat
import seaborn
import pandas
from math import ceil
from src.math import dslr_mean
from random import Random
import random

import sys

import matplotlib.pyplot as plt

from src.reader import Reader
from src.student import Student

houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]
features = [
		"Arithmancy",
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
		"Flying"]

def dslr_histogram(students_df: pandas.DataFrame):
	figure = plt.figure(1, )
	columns = 4
	rows = (len(features) / columns).__ceil__()
	for i, feature in enumerate(features):
		figure.add_subplot(rows, columns, i + 1)
		seaborn.histplot(data=students_df,
			x = feature,
			hue = "Hogwarts House"
		)
	plt.show()




if __name__ == "__main__":
	if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv") :
		print("Program only takes one .csv file")
		sys.exit()
	df = pandas.read_csv(sys.argv[1])
	dslr_histogram(df)
