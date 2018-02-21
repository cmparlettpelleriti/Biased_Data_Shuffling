import csv, random
import numpy as np
import pandas as pd
# import models as ms
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt
print("OKAY===============================================================")
mus = [0,1]
sigs  = [1,1]
proportion = [1,99]
n = 10000

dfALL = pd.DataFrame(columns = ['label','vars'])
for i in range(0, len(proportion)):
    k = int(n/sum(proportion)* proportion[i])
    dist1 = np.random.normal(size = k, loc = mus[i], scale = sigs[i])
    ns = np.repeat(i,k)
    df = pd.DataFrame({'label':ns,'vars':dist1})
    dfALL = pd.concat([dfALL,df])


train_x, test_x, train_y, test_y = train_test_split(dfALL['vars'], dfALL['label'],train_size=0.7)
train_y = train_y.astype('int')
test_y = test_y.astype('int')
test_x = test_x.reshape(-1,1)
train_x = train_x.reshape(-1,1)
LogReg = LogisticRegression(class_weight = 'balanced')
y_pred = LogReg.fit(train_x, train_y)
y_pred = LogReg.predict(test_x)
y_predp = LogReg.predict_proba(test_x)
cm = metrics.confusion_matrix(test_y, y_pred)
auc = metrics.roc_auc_score(test_y,y_pred)
roc = metrics.roc_curve(test_y,y_pred)
print(auc)
print(cm)
# plt.plot(roc[0],roc[1])
