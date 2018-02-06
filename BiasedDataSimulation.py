import csv, random
import numpy as np
import pandas as pd
'''The purpose of this script is to

1) Generate either related or random outputs from random data
(both continuous and discrete data --> discrete outputs)

2) Use label switching/bootstrapping to generate distributions
of theoretical values for AUC'''


############ Functions ##################
#------- Label Shifting --------------------
def labelFlip(df,colName):
    '''Randomly Shuffles Classifications'''
    flippable = list(df[colName])
    random.shuffle(flippable)
    flippable = pd.Series(flippable)
    df[colName] = flippable.values
    print(head(df))
    return df
#------- Create Data --------------------
def simContinuous(mus, sds, n = 10, cols = []):
    '''Simulates continuous data columns, these
    aren't assumed to be correlated...should I add that? Maybe. IDK.'''
    if cols == []:
        for i in range(0,len(coefs)):
            cols.append("c" + str(i))
    coefs = np.array(coefs)
    mus = np.array(mus)
    sds = np.array(sds)
    allNs = sds * np.random.randn(n,len(coefs)) + mus
    allNs = np.matrix(allNs)
    print(allNs)
    return allNs


def simDiscrete(props, opts, n = 10, cols = []):
    '''simulates discrete data columns, assumed not to be related'''
    if cols == []:
        for i in range(0,len(props)):
            cols.append("d" + str(i))
    ns = []
    for i in range(0,len(props)):
        col = np.random.choice(a = opts[i], size = n, p = props[i])
        ns.append(col)
    n = np.matrix(ns)
    n = n.transpose()
    print(n)
    return n

def combineCandD(m1,m2):
    '''combine continuous and discrete variables when necessary'''
    together = np.concatenate((m1, m2), axis=1)
    print(together)
    return together

def genRelatedOut(coefs,df):
    # outPut = np.dot(allNs, coefs)
    # outPut = pd.Series(outPut)
    # #print("OUT", outPut, len(outPut))
    # data = pd.DataFrame(allNs, columns = cols)
    # data = data.assign(out = outPut)
    # print(data)
    pass
def genRandomOut(df):
    pass
a = simContinuous([1,1,1],[0.1,0.5,0.001], n = 10)
b = simDiscrete([[0.5,0.5],[0.1,0.9]], [[0,1],[2,4]], n = 10)
combineCandD(a,b)
#------- Distribution Generation --------------------
