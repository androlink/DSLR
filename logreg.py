import numpy
from src.ova import train_ova
import pandas

from src.normalize_features import normalizeDataFrame
import src.normalize_features
import src.ova

df = pandas.read_csv("data/dataset_train.csv")

y = df['Hogwarts House']

X = normalizeDataFrame(df)

W,B = train_ova(X.to_numpy(dtype=numpy.float64), y)

print(W)
print(B)
