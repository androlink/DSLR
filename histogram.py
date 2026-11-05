from matplotlib.axes import Axes
import seaborn
import pandas

import sys

import matplotlib.pyplot as plt
from src.features_enum import Features
from src.visualizer_cli import VisualizerCli
from src.visualizer import Visuliazer

def dslr_histogram(students_df: pandas.DataFrame):
  visualizer = Visuliazer(students_df)
  for i, feature in enumerate(Features):
    visualizer.addHistogram(i, x=feature)
  visualizer.show()

if __name__ == "__main__":
  cli = VisualizerCli()
  
  if not cli.filePath.endswith(".csv") :
    print("Program only takes one .csv file as argument")
    sys.exit()
  df = pandas.read_csv(sys.argv[1])
  dslr_histogram(df)
