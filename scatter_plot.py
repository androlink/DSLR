import matplotlib.pyplot as plt
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
  
  fig = plt.figure(1, layout='constrained')
  
  
  columns = 4
  rows = (len(Features) / columns).__ceil__()
  
  featuresName = [f for f in Features]
  
  markerSize = 4.2
  
  for i in range(1, len(Features)+1):
    feature = featuresName[i-1]
    fig.add_subplot(rows, columns, i)
    
    sp = ScaterPlot(reader, feature)
    
    
    plt.scatter(sp.gryffindorX, sp.gryffindorY, color='gold', label='gryffindor', s=markerSize)
    plt.scatter(sp.slytherinX, sp.slytherinY, color='green', label='slytherin', s=markerSize)
    plt.scatter(sp.ravenclawX, sp.ravenclawY, color='blue', label='ravenclaw', s=markerSize)
    plt.scatter(sp.hufflepuffX, sp.hufflepuffY, color='red', label='hufflepuff', s=markerSize)
    
    plt.xlabel("Index")
    plt.ylabel("Grade")
    plt.title(feature)

  fig.legend(["gryffindor", "slytherin", "ravenclaw", "hufflepuff"], loc='lower right')
  fig.suptitle('Scatter plots')
  plt.show()
    
  