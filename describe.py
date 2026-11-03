import sys
import pandas

from src.reader import Reader

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


if __name__ == '__main__':
  app = CommandLine()
  
  if not app.filePath.endswith(".csv") :
    print("describe.py only takes one .csv file as argument")
    exit()
    
  def applyRound(value) -> float:
    if app.roundUp != None:
      return round(value, app.roundUp)
    return value
  
  reader = Reader(app.filePath)
  
  fields = [
    'arithmancy', 
    'astronomy',  
    'herbology',  
    'defense',  
    'divination', 
    'muggleStudies',  
    'ancientRunes', 
    'historyOfMagic', 
    'transfiguration',  
    'potions',  
    'careOfMagicalCreatures', 
    'charms', 
    'flying', 
  ]
  
  for value in app.include:
    if value not in fields:
      app.include.remove(value)
  if app.include == []:
    app.include = fields
  
  data = {}
  
  for field in app.include:
    feature = reader.listOfProperty(field)
    l = []
    l.append(len(feature))
    l.append(applyRound(dslr_math.dslr_mean(feature)))
    l.append(applyRound(dslr_math.dslr_stddev(feature)))
    l.append(applyRound(dslr_math.dslr_min(feature)))
    l.append(applyRound(dslr_math.dslr_quartile(feature, .25)))
    l.append(applyRound(dslr_math.dslr_quartile(feature, .50)))
    l.append(applyRound(dslr_math.dslr_quartile(feature, .75)))
    l.append(applyRound(dslr_math.dslr_max(feature)))
    l.append(applyRound(dslr_math.dslr_count_none(feature)))
    data[field] = l

  df = pandas.DataFrame(data=data, index=["count", "mean", "std", "min", "25%", "50%", "75%", "max", "count_none"])
  print(df)
  
  
  