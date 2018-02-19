import csv, random
import numpy as np
import pandas as pd
'''The purpose of this script is to

1) Generate either related or random outputs from random data
(both continuous and discrete data --> discrete outputs)

2) Use label switching/bootstrapping to generate distributions
of theoretical values for AUC'''


############ Functions ##################
class SDO(object):
    #shuffalable data object
    '''cov: can be  one or two dimensional'''
    def __init__(self, n = 10, cols = [], mus = [],cov = [], props = [], opts = []):
        self.n = n
        self.data = None
        self.Cdata = None
        self.Ddata = None
        self.cols = cols
        #--------------------
        if self.cols == []:
            self.cols = []
            for i in range(0,len(mus)):
                self.cols.append("c" + str(i))
        else:
            self.cols = cols
        #--------------------
        self.mus = mus
        self.cov = cov
        self.props = props
        self.opts = opts
        #--------------------
        if mus != []:
            self.simContinuous()
        if props != []:
            self.simDiscrete()
        if self.Cdata != None and self.Ddata != None:
            self.combineCandD()
        #--------------------
    def simContinuous(self):
        '''Simulates continuous data columns, these
        aren't assumed to be correlated...should I add that? Maybe. IDK.'''
        self.mus = np.array(mus)
        self.cov = np.array(cov)
        allNs = self.cov * np.random.randn(n,len(self.mus)) + self.mus
        self.Cdata = np.matrix(allNs)
    def simDiscrete(self):
        '''simulates discrete data columns, assumed not to be related'''
        ns = []
        for i in range(0,len(self.props)):
            col = np.random.choice(a = self.opts[i], size = self.n, p = self.props[i])
            ns.append(col)
        n = np.matrix(ns)
        n = n.transpose()
        self.Ddata = n
    def combineCandD(self):
        '''combine continuous and discrete variables when necessary'''
        self.data = np.concatenate((self.Cdata, self.Ddata), axis=1)
    def labelFlip(self,flipCol):
        '''Randomly Shuffles Classifications'''
        flippable = list(self.data[colName])
        random.shuffle(flippable)
        flippable = pd.Series(flippable)
        self.data[colName] = flippable.values
    def mvSimCont(self):
        '''Simulating multivariate continuous continuous data
        '''
        self.Cdata = np.random.multivariate_normal(self.mus,self.cov,size = n)
        pass
    def mvSimDisc(self,thresholds = None):
        d = np.random.multivariate_normal(self.mus, self.cov, size = n)
        d = d.transpose()
        print(d)
        for i in d:


        pass
