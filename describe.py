import pandas

from src.features_enum import Features

import src.dslr_math as dslr_math

import argparse

class CommandLine:
  roundUp: int | None = None
  filePath: str
  include: list[str] = []
  def __init__(self):
      parser = argparse.ArgumentParser(description = "")
      parser.add_argument('filePath', type = str)
      parser.add_argument("-r", "--round", help = "Round values to X decimal", required = False, default = None, type=int)
      parser.add_argument("-i", "--include", help = "Include column with names", nargs='+', required = False, default = None, type=str)
      
      argument = parser.parse_args()
      
      self.filePath = argument.filePath
      
      if argument.round:
        self.roundUp = argument.round
      if argument.include:
        self.include = argument.include

def applyRound(value) -> float:
  if app.roundUp != None:
    return round(value, app.roundUp)
  return value
  
if __name__ == '__main__':
  app = CommandLine()
  
  if not app.filePath.endswith(".csv") :
    print("describe.py only takes one .csv file as argument")
    exit()
  
  dataFrame: pandas.DataFrame = pandas.read_csv(app.filePath)
  
  for value in app.include:
    if value not in Features:
      app.include.remove(value)
  if app.include == []:
    app.include = [f for f in Features]
  
  data = {}
  
  for feature in app.include:
    if feature == Features.hogwartsHouse: continue
    countNone = dataFrame.get(feature).isna().tolist().count(True)
    values = dataFrame.get(feature).dropna().tolist()
    l = []
    l.append(len(values))
    l.append(applyRound(dslr_math.dslr_mean(values)))
    l.append(applyRound(dslr_math.dslr_stddev(values)))
    l.append(applyRound(dslr_math.dslr_min(values)))
    l.append(applyRound(dslr_math.dslr_quartile(values, .25)))
    l.append(applyRound(dslr_math.dslr_quartile(values, .50)))
    l.append(applyRound(dslr_math.dslr_quartile(values, .75)))
    l.append(applyRound(dslr_math.dslr_max(values)))
    l.append(countNone)
    data[feature] = l

  df = pandas.DataFrame(data=data, index=["count", "mean", "std", "min", "25%", "50%", "75%", "max", "count_none"])
  print(df)
  
  
  