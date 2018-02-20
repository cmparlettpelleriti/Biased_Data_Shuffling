#------- Label Shifting --------------------
def labelFlip(df,colName):
    '''Randomly Shuffles Classifications'''
    flippable = list(df[colName])
    random.shuffle(flippable)
    flippable = pd.Series(flippable)
    df[colName] = flippable.values
    print(head(df))
    return df

def simContinuous(mus, cov, n = 10, cols = []):
    '''Simulates continuous data columns, these
    aren't assumed to be correlated...should I add that? Maybe. IDK.'''
    if cols == []:
        for i in range(0,len(coefs)):
            cols.append("c" + str(i))
    coefs = np.array(coefs)
    mus = np.array(mus)
    cov = np.array(cov)
    allNs = cov * np.random.randn(n,len(coefs)) + mus
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
# a = simContinuous([1,1,1],[0.1,0.5,0.001], n = 10)
# b = simDiscrete([[0.5,0.5],[0.1,0.9]], [[0,1],[2,4]], n = 10)
# combineCandD(a,b)
#------- Distribution Generation --------------------

#QUESTIONS
# 1) Do we want to simulate two multivariate sets, one for 0 and one for 1?
# OR do we want it all to be the same mv dist and let the model decide?
# 2) AUC values
# 3) We want to know what the difference is between
# label shuffling with non model generated and model generated data...

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
        print("STARTING")
        self.n = n
        self.data = None
        self.Cdata = None
        self.Ddata = None
        self.cols = cols
        self.mus = mus
        self.cov = cov
        self.props = props
        self.opts = opts
        if mus != []:
            # self.simContinuous()
            self.mvSimCont()
            #need to account for multiple groups?
        if props != []:
            self.simDiscrete()
        if type(self.Cdata) == type(self.Ddata):
            self.combineCandD()
        if self.cols == []:
            self.cols = []
            for i in range(0,len(mus)):
                self.cols.append("c" + str(i))
        else:
            self.cols = cols
        #--------------------
    def simContinuous(self):
        '''Simulates continuous data columns, these
        aren't assumed to be correlated...should I add that? Maybe. IDK.'''
        self.mus = np.array(self.mus)
        self.cov = np.matrix(self.cov)
        allNs = self.cov * np.random.randn(len(self.mus),self.n)
        for ns in range(0,len(allNs)):
            allNs[ns] += self.mus[ns]
        self.Cdata = np.matrix(allNs)
        self.Cdata = self.Cdata.T
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
        self.Cdata = np.random.multivariate_normal(np.array(self.mus),np.matrix(self.cov),size = self.n)
        pass
    def mvSimDisc(self,thresholds = None):
        pass
        # d = np.random.multivariate_normal(self.mus, self.cov, size = n)
        # d = d.transpose()
        # print(d)
        # for i in d:
    def RandomLabels(self):
        choices = []
        for i in range(0,len(opts)):
            pass

###############TEST##############################

mySDO = SDO(n = 100,mus = [10,10,15], cov = [[1,.5,.45],[.5,1,.45],[.45,.5,1]])
print(mySDO.Cdata)

#b = ms.logistic_regression(mySDO.Cdata)
# b = ms.multi_layer_perceptron(mySDO.Cdata)
# print(b)
