```python
import random
import pandas as pd
from collections import Counter

simulations = []
input = [2, 3]     

def inputData(y):       #makes the input list which we'll compare to simulated results
    remain = y
    for i in range(len(input)):
        remain = remain - (len(input)+1-i) * input[i]
    input.append(remain)

def simulate(y, z):     #refreshes y times from a pool of size z / returns one input data format
    list = []
    for i in range(y):
        p = random.randint(1, z)
        list.append(p)
    freq = Counter(list)
    df = pd.DataFrame.from_dict(freq, orient='index')
    c = Counter(df[0])
    c = pd.DataFrame.from_dict(c, orient='index').sort_index(axis=0, ascending = False)
    c = c[0].to_list()
    
    simulations.append(c)

def prevalence(x, y, z): #runs x simulations of y refreshes from a pool of z comics
    inputData(y)
    for i in range(x):
        simulate(y,z)
    print(simulations.count(input)/x)

prevalence(100000, 100, 1000)


```

    0.00191

