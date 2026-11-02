
import matplotlib.pyplot as plt

from src.student import Student

houses = ["Ravenclaw", "Slytherin", "Gryffindor", "Hufflepuff"]

def dslr_histogram(students: list[Student]):
	house_data: dict[str, list[Student]] = {}
	for house in houses:
		house_data[house] = [s for s in students if s.house == house]




if __name__ == "__main__":
	pass
