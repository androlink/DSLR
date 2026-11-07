
from src.normalize_features import prepare_dataframe, min_max_scale
import numpy
from src.ova import train_ova, predict
import pandas

df = pandas.read_csv("data/dataset_train.csv")

y = df['Hogwarts House']

X = df.copy()

X = prepare_dataframe(X)
X = min_max_scale(X)
X = X.to_numpy(dtype=numpy.float64)

W,B,C = train_ova(X, y)

print(W)
print(B)
print(C)

X = df.filter(pandas.col('Hogwarts House') == 'Gryffindor')
X = X.drop(columns=['Index', 'Last Name' ,'First Name', 'Birthday', 'Hogwarts House'])
X = X.replace('Left', -1).replace('Right', 1)
X = X.fillna(0)
X = min_max_scale(X)
print(X)

X = X.to_numpy(dtype=numpy.float64)
r = predict(X, W, B, C)

print(r)
