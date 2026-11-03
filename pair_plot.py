import matplotlib.pyplot as plt
import pandas
from src.reader import Reader
from src.features_enum import Features
from src.visualizer_cli import VisualizerCli

class ScaterPlot():
  reader: Reader
  feature: Features
  
  gryffindorX: list[int]
  gryffindorY: list[float]
  hufflepuffX: list[int]
  hufflepuffY: list[float]
  ravenclawX: list[int]
  ravenclawY: list[float]
  slytherinX: list[int]
  slytherinY: list[float]
    
  
  def __init__(self, reader: Reader, feature: Features):
    self.reader = reader
    self.feature = Features
    
    self.gryffindorY = []
    self.slytherinY = []
    self.ravenclawY = []
    self.hufflepuffY = []
    
    for student in reader.students:
      match student.house:
        case 'Gryffindor':
          self.gryffindorY.append(student[feature])
        case 'Slytherin':
          self.slytherinY.append(student[feature])
        case 'Ravenclaw':
          self.ravenclawY.append(student[feature])
        case 'Hufflepuff':
          self.hufflepuffY.append(student[feature])
    self.gryffindorX = [i for i in range(len(self.gryffindorY))]
    self.slytherinX = [i for i in range(len(self.slytherinY))]
    self.ravenclawX = [i for i in range(len(self.ravenclawY))]
    self.hufflepuffX = [i for i in range(len(self.hufflepuffY))]
    pass

if __name__ == '__main__':
  cli = VisualizerCli()
  
  if not cli.filePath.endswith(".csv") :
    print("scatter_plot.py only takes one .csv file as argument")
    exit()

  reader = Reader(cli.filePath)
  
  data: pandas.DataFrame = pandas.DataFrame({f: reader.listOfProperty(f) for f in Features})
  num_features = len(Features)
  
  fig: plt.Figure
  axes: plt.Axes
  fig, axes = plt.subplots(num_features, num_features, figsize=(10, 10))
  markerSize = 4.2
  
  fig.set_layout_engine('constrained')
  for i in range(num_features):
    for j in range(num_features):
      ax: plt.Axes = axes[i, j]
      if i == j:
          ax.hist(data.iloc[:, i], bins=15, color='skyblue', edgecolor='black')
      else:
          ax.scatter(data.iloc[:, j], data.iloc[:, i], alpha=0.7, s=10, color="blue")

      if j == 0:
          ax.set_ylabel(data.columns[i], fontsize=10)
      if i == num_features - 1:
          ax.set_xlabel(data.columns[j], fontsize=10)

      # Remove ticks for a cleaner look
      ax.set_xticks([])
      ax.set_yticks([])

  plt.show()
    
  