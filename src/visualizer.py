from pandas import DataFrame

from src.features_enum import Features
from matplotlib import pyplot as plt
from matplotlib.pyplot import Axes
from matplotlib.figure import Figure
from seaborn import scatterplot, histplot


class Visuliazer():
  columns = 4
  rows = (len(Features) / columns).__ceil__()
  fig: Figure
  ax: Axes
  
  markerSize = 4.2
  fontSize = 7.5 
  
  hue: str
  showTicks: bool
  def __init__(self, data: DataFrame, dropedColumns = ['Last Name' ,'First Name', 'Best Hand', 'Birthday'], hue="Hogwarts House", showTicks = True):
    self.data = data
    self.data.drop(columns=dropedColumns)
    
    self.fig = plt.figure(1)
    self.fig.set_layout_engine('compressed')
    
    self.hue = hue
    self.showTicks = showTicks
    pass
  
  def addScatterPlot(self, index: int, x: str, y: str, xLabel: str | None = None, yLabel: str | None = None, title: str | None = None) -> plt.Axes:
    self.fig.add_subplot(self.rows, self.columns, index + 1)
    self.ax = scatterplot(self.data, x=x, y=y, hue=self.hue, size=self.markerSize, legend=False)
    self.updateAxesOption(xLabel, yLabel, title)
    return self.ax
    
  def addHistogram(self, index: int, x: str, bins: int | str = 'auto', xLabel: str | None = None, yLabel: str | None = None, title: str | None = None) -> plt.Axes:
    self.fig.add_subplot(self.rows, self.columns, index + 1)
    self.ax = histplot(self.data, x=x, bins=bins, hue=self.hue, legend=False)
    self.updateAxesOption(xLabel, yLabel, title)
    return self.ax
  
  def updateAxesOption(self, xLabel: str | None = None, yLabel: str | None = None, title: str | None = None):
    if xLabel is not None: self.ax.set_xlabel(xLabel, size=self.fontSize)
    if yLabel is not None: self.ax.set_ylabel(yLabel, size=self.fontSize)
    if self.showTicks == False:
      self.ax.set_xticks([])
      self.ax.set_yticks([])
    if title is not None: self.ax.set_title(title)
  
  def show(self):
    self.fig.legend()
    self.fig.set_size_inches(20, 20)
    plt.show()