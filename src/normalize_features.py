from pandas import DataFrame
from src.dslr_math import dslr_normalize
from src.features_enum import Features

def normalizeDataFrame(df: DataFrame):
  fields: list[str] = [f.value for f in Features]
  fields.append('Best Hand')
  fields.remove('Hogwarts House')
  df = df.drop(columns=['Index', 'Last Name' ,'First Name', 'Birthday', 'Hogwarts House'])
  df = df.replace('Left', -1).replace('Right', 1)
  data = {}
  for field in fields:
    l = df.get(field).fillna(0).tolist()
    data[field] = dslr_normalize(l)
  return DataFrame(data)