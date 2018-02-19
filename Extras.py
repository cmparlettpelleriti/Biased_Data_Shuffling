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
