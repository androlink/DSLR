import matplotlib.pyplot as plt
import pandas
from src.reader import Reader
from src.features_enum import Features
from src.visualizer_cli import VisualizerCli
import seaborn

if __name__ == '__main__':
  cli = VisualizerCli()
  
  if not cli.filePath.endswith(".csv") :
    print("scatter_plot.py only takes one .csv file as argument")
    exit()
  
  data: pandas.DataFrame = pandas.read_csv(cli.filePath)
  data = data.drop(columns=['Index', 'Last Name' ,'First Name', 'Best Hand', 'Birthday'])
  numFeatures = len(Features)
  
  fig = plt.figure(1)
  fig.set_layout_engine('compressed')
  columns = rows = numFeatures
  
  markerSize = 4.2
  featuresName = [f for f in Features]
  fontSize = 7.5
  # For some reason the color order is shifted :(
  custom_palette = {
    "Gryffindor": "green",
    "Slytherin": "red",
    "Ravenclaw": "blue",
    "Hufflepuff": "orange",
  }
  i = 0
  for fi in Features:
    if fi == Features.hogwartsHouse: 
      i += 1
      continue
    j = 0
    for fj in Features:
      if fj == Features.hogwartsHouse: 
        j += 1
        continue
      fig.add_subplot(rows, columns, ((numFeatures * i) + j) + 1)
      ax: plt.Axes

      if i == j:
          ax = seaborn.histplot(data,
            x = fi,
            bins=15,
            hue="Hogwarts House",
            palette=custom_palette,
            legend=False,
            edgecolor='black'
          )
      else:
          ax = seaborn.scatterplot(data,
            x = fj,
            y = fi ,
            hue="Hogwarts House",
            palette=custom_palette,
            legend=False,
            size=markerSize
          )
      
      ax.set_xlabel('')
      ax.set_ylabel('')
      if j == 0:
          ax.set_ylabel(fi, size=fontSize)
      # `-2` and not `-1` due to hogwartsHouse being ignored
      if i == numFeatures - 2:
          ax.set_xlabel(fj, size=fontSize)

      ax.set_xticks([])
      ax.set_yticks([])
      j += 1
    i += 1
  fig.set_size_inches(20, 20)
  plt.figlegend(custom_palette, loc='lower right')
  plt.show()
    
  