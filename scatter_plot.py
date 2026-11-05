import pandas
from src.features_enum import Features
from src.visualizer_cli import VisualizerCli
from src.visualizer import Visuliazer

if __name__ == '__main__':
  cli = VisualizerCli()
  
  if not cli.filePath.endswith(".csv") :
    print("scatter_plot.py only takes one .csv file as argument")
    exit()
    
  visualizer = Visuliazer(pandas.read_csv(cli.filePath))
  
  for i, feature in enumerate(Features):
    if feature == Features.hogwartsHouse: 
      continue
    visualizer.addScatterPlot(index=i, x='Index', y=feature, yLabel="Grade", title=feature)
  visualizer.show()    
  