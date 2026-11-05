import pandas
from src.features_enum import Features
from src.visualizer_cli import VisualizerCli
from src.visualizer import Visuliazer

if __name__ == '__main__':
  cli = VisualizerCli()
  
  if not cli.filePath.endswith(".csv") :
    print("scatter_plot.py only takes one .csv file as argument")
    exit()
    
  visuliazer = Visuliazer(pandas.read_csv(cli.filePath), ['Index', 'Last Name' ,'First Name', 'Best Hand', 'Birthday'], showTicks=False)
  visuliazer.rows = visuliazer.columns = numFeatures = len(Features)
  
  for i, fi in enumerate(Features):
    if fi == Features.hogwartsHouse: 
      continue
    for j, fj in enumerate(Features):
      if fj == Features.hogwartsHouse: 
        continue
      # `-2` and not `-1` due to hogwartsHouse being ignored
      xLabel = fj if i == numFeatures - 2 else ''
      yLabel = fi if j == 0 else ''
      idx = (numFeatures * i) + j

      if i == j:
          visuliazer.addHistogram(index=idx, x=fi, bins=15, xLabel=xLabel, yLabel=yLabel)
      else:
          visuliazer.addScatterPlot(index=idx, x=fj, y=fi, xLabel=xLabel, yLabel=yLabel)

  visuliazer.show()
    
  