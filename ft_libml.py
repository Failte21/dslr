import math
import pandas as pd

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

def percentile(v, p): #TODO: Fix
    d = sorted(v.dropna())
    n = len(d)
    x = p * ((n - 1) + 1)
    i = int(x)
    mod = x % 1
    return d[i] + (mod * (d[i + 1] - d[i]))

def per_25(v):
    return percentile(v, 0.25)

def per_50(v):
    return percentile(v, 0.5)

def per_75(v):
    return percentile(v, 0.75)