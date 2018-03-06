import csv, random
import numpy as np
import pandas as pd
import models as ms
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
print("OKAY===============================================================")
mu2 = 10
sig1 = 1
sig2 = 1
proportion = [1,9]
n = 1000

# dfALL = pd.DataFrame(columns = ['label', 'val', 'val2'])
dfALL = pd.DataFrame(columns = ['label', 'val'])
for i in range(0, len(proportion)):
    k = int(n/sum(proportion)* proportion[i])
    dist1 = np.random.normal(loc = 0, scale = sig1, size = k)
    # dist2 = np.random.normal(loc = 0, scale = sig1, size = k)
    ns = np.repeat(i,k)
    # df = pd.DataFrame({'label': ns, 'val': dist1, 'val2': dist2})
    df = pd.DataFrame({'label': ns, 'val': dist1})
    dfALL = pd.concat([dfALL,df])

#train_x, test_x, train_y, test_y = train_test_split(dfALL[['val', 'val2']], dfALL['label'], train_size=0.7)
train_x, test_x, train_y, test_y = train_test_split(dfALL['val'], dfALL['label'],train_size=0.7)
train_y = train_y.astype('int')
test_y = test_y.astype('int')
LogReg = LogisticRegression(class_weight = 'balanced')
y_pred = LogReg.fit(train_x, train_y)
y_pred = LogReg.predict(test_x)
y_predp = LogReg.predict_proba(test_x)
cm = metrics.confusion_matrix(test_y, y_pred)
auc = metrics.roc_auc_score(test_y,y_pred)
roc = metrics.roc_curve(test_y,y_pred)
print(auc)
print(cm)
