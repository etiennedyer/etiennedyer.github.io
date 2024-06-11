```python
import random
import pandas as pd
import seaborn as sns
from collections import Counter

input = [2, 3]     
simulations = []

def inputData(y):       #makes the input list which we'll compare to simulated results
    global input
    remain = y
    for i in range(len(input)):
        remain = remain - (len(input)+1-i) * input[i]
    input.append(remain)

def simulate(y, z):     #refreshes y times from a pool of size z / returns one input data format
    global simulations
    global list
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

def prevalence(x, y, z): #runs x simulations of y refreshes from a pool of z objects
    global prev
    simulations.clear()
    for i in range(x):
        simulate(y,z)
    prev = (simulations.count(input)/x)
    return(prev)

def runthru(): #runs through all possible values in increments of the range incrents and graphs results
    X = []
    y = []
    global simulations
    for i in range(500, 1500, 50):
        simulations.clear()
        x = prevalence(1000000, 100, i)
        print(i, prev)
        X.append(i)
        y.append(prev)
    d = {'X': X, 'y': y}   
    df = pd.DataFrame(data = d)
    sns.barplot(data=df, x="X", y="y")

def runagain(p, k): #recursive search function
    global int
    running = True
    while running == True:
        x1 = prevalence(k, 100, int)
        x2 = prevalence(k, 100, int-p)
        x3 = prevalence(k, 100, int+p)
        print('x1', x1, 'x2', x2, 'x3', x3)
        if x2 < x1 < x3:
            int = int+p
        if x2 > x1 > x3:
            int = int-p
        if x3 > x2 > x1:
            int = int+p
        if x2 < x1 and x3 < x1:
            print(int, 'is optimal at a precision of', p, '!')
            running = False
            if p/2 > 1:
                p = round(p/2)
                runagain(p, k)
            else: 
                (print(int, 'is globally optimal!'))
        print(int)

def runsmart(p, k): #main search function, 
    global int
    inputData(100)
    running = True
    int = random.randint(1, 2000)
    print(int)
    while running == True:
        x1 = prevalence(k, 100, int)
        x2 = prevalence(k, 100, int-p)
        x3 = prevalence(k, 100, int+p)
        print('x1', x1, 'x2', x2, 'x3', x3)
        if x2 < x1 < x3 or x3 > x2 > x1:
            int = int+p
        if x2 > x1 > x3:
            int = int-p
        if x1 == x2 == x3 == 0.0:
            int = random.randint(1, 2000)
        if x2 < x1 and x3 < x1:
            print(int, 'is optimal at a precision of', p, '!')
            running = False
            if p/2 > 1:
                p = round(p/2)
                runagain(p, k)
        print(int)
    
runsmart(300, 100000)

```

    417
    x1 0.00108 x2 0.0 x3 0.00295
    717
    x1 0.00266 x2 0.00107 x3 0.00189
    717 is optimal at a precision of 300 !
    x1 0.00285 x2 0.00243 x3 0.00241
    717 is optimal at a precision of 150 !
    x1 0.00279 x2 0.00292 x3 0.00276
    642
    x1 0.00345 x2 0.00278 x3 0.00296
    642 is optimal at a precision of 75 !
    x1 0.00294 x2 0.00276 x3 0.00281
    642 is optimal at a precision of 38 !
    x1 0.00293 x2 0.00283 x3 0.00295
    661
    x1 0.00284 x2 0.00266 x3 0.00292
    680
    x1 0.00298 x2 0.00295 x3 0.00286
    680 is optimal at a precision of 19 !
    x1 0.00263 x2 0.00284 x3 0.00283
    680
    x1 0.00285 x2 0.00281 x3 0.00301
    690
    x1 0.00304 x2 0.00295 x3 0.0034
    700
    x1 0.00273 x2 0.0027 x3 0.00303
    710
    x1 0.00299 x2 0.00326 x3 0.00269
    700
    x1 0.00277 x2 0.00324 x3 0.00281
    700
    x1 0.00276 x2 0.00297 x3 0.00302
    710
    x1 0.0027 x2 0.00271 x3 0.00306
    720
    x1 0.00264 x2 0.00318 x3 0.00268
    720
    x1 0.00279 x2 0.00285 x3 0.00286
    730
    x1 0.00272 x2 0.00301 x3 0.00306
    740
    x1 0.00283 x2 0.0028 x3 0.00302
    750
    x1 0.003 x2 0.00304 x3 0.00261
    740
    x1 0.0029 x2 0.00302 x3 0.00294
    740
    x1 0.00319 x2 0.0028 x3 0.00294
    740 is optimal at a precision of 10 !
    x1 0.00268 x2 0.00273 x3 0.00298
    745
    x1 0.00288 x2 0.00277 x3 0.00264
    745 is optimal at a precision of 5 !
    x1 0.00272 x2 0.00318 x3 0.0029
    745
    x1 0.00304 x2 0.0027 x3 0.00283
    745 is optimal at a precision of 2 !
    745 is globally optimal!