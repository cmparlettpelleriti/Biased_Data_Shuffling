import csv, random
import numpy as np
import pandas as pd
import models as ms
import sklearn

mu2 = 10
sig1 = 1
sig2 = 1
proportion = [1,9]
n = 1000

dfALL = pd.DataFrame(columns = ['label', 'val'])
for i in range(0, len(proportion)):
    k = int(n/sum(proportion)* proportion[i])
    dist1 = np.random.normal(loc = 0, scale = sig1, size = k)
    ns = np.repeat(i,k)
    df = pd.DataFrame({'label': ns, 'val': dist1})
    dfALL = pd.concat([dfALL,df])
print(dfALL)

LogReg = LogisticRegression(class_weight = 'balanced')
y_pred = LogReg.fit(train_x, train_y)
y_pred = LogReg.predict(test_x)
cm = metrics.confusion_matrix(test_y, y_pred)
