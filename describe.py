import sys
import pandas

from src.reader import Reader

import src.dslr_math as dslr_math


if __name__ == '__main__':
  if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv") :
    print("describe.py only takes one .csv file as argument")
    exit()
  
  reader = Reader(sys.argv[1])
  
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
  
  data = {}
  
  for field in fields:
    feature = reader.listOfProperty(field)
    l = []
    l.append(len(feature))
    l.append(dslr_math.dslr_mean(feature))
    l.append(dslr_math.dslr_stddev(feature))
    l.append(dslr_math.dslr_min(feature))
    l.append(dslr_math.dslr_quartile(feature, .25))
    l.append(dslr_math.dslr_quartile(feature, .50))
    l.append(dslr_math.dslr_quartile(feature, .75))
    l.append(dslr_math.dslr_max(feature))
    data[field] = l

  print(pandas.DataFrame(data=data, index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"]))
  
  
  