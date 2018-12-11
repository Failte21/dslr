import math

def ft_count(x):
    return len(x)

def ft_mean(x):
    return sum(x) / ft_count(x)

def ft_min(x):
    curr_min = x[0]
    x_len = len(x)
    i = 0
    while i < x_len:
        if x[i] < curr_min:
            curr_min = x[i]
            i = 0
        i += 1
    return curr_min

def ft_max(x):
    curr_max = x[0]
    x_len = len(x)
    i = 0
    while i < x_len:
        if x[i] > curr_max:
            curr_max = x[i]
            i = 0
        i += 1
    return curr_max

def ft_std(x):
    mean = ft_mean(x)
    count = ft_count(x)
    return math.sqrt(sum((x - mean)**2) / (count - 1))

def ft_percentile(p): #TODO: Secure for wrong values
    def h(v):
        n = len(v)
        x = ((p / 100) * (n - 1))
        f = int(x)
        mod = x % 1
        return v[f] + mod * (v[f] - v[f - 1])
    return (h)