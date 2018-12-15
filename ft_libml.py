import math
import pandas as pd
from sklearn import preprocessing
from load_datas import courses

#TODO: remove sklearn
def normalize(df):
	x = df.values #returns a numpy array
	min_max_scaler = preprocessing.MinMaxScaler()
	x_scaled = min_max_scaler.fit_transform(x)
	return pd.DataFrame(x_scaled, columns=courses)

def count(x):
    d = x.dropna()
    return len(d)

def mean(x):
    d = x.dropna()
    return sum(d) / count(d)

def min(x):
    d = sorted(x.dropna())
    return d[0]

def max(x):
    d = sorted(x.dropna())
    return d[len(d) - 1]

def std(x):
    d = sorted(x.dropna())
    m = mean(x)
    c = count(x)
    return math.sqrt(sum((d - m)**2) / (c - 1))

def percentile(v, p): #TODO: np percentile: be able to explain
    d = sorted(v.dropna())
    n = len(d)
    x = p * (n - 1)
    i = int(x)
    mod = x % 1
    return d[i] + (mod * (d[i + 1] - d[i]))

def per_25(v):
    return percentile(v, 0.25)

def per_50(v):
    return percentile(v, 0.5)

def per_75(v):
    return percentile(v, 0.75)