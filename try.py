import csv, random
import numpy as np
import pandas as pd
# import models as ms
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

print("STARTED--------------------------------")

fns = ["auc", "TP", "FP","FN","TN", "Pos Prop",
"n", "mu1", "mu2", "deltamu","sig1","sig2", "deltasig", "effectsize", "pospred"]
writer = csv.DictWriter(open("outputs.csv",'w'), fieldnames = fns)
writer.writeheader()


ps = [[1,9],[1,99]]
m = [[0,(i/10)]for i in range(0,100)]
s =  [[1,(i/100)] for i in range(100,1000,100)]
s += [[1,11-(i/100)] for i in range(100,1000,100)]
# for i in range(100,1000,50):
#     s.append([1,(i/100)])
#     s.append([1,11-(i/100)])


for n in range(500,1500,100):
    print(n)
    for proportion in ps:
        for sigs in s:
            for mus in m:
                for i in range(0,1):
                    # print("OKAY===============================================================")
                    # mus = [0,10]
                    # sigs  = [1,1]
                    # proportion = [1,9]
                    # n = 10000

                    dfALL = pd.DataFrame(columns = ['label','vars'])
                    for i in range(0, len(proportion)):
                        k = int(n/sum(proportion)* proportion[i])
                        dist1 = np.random.normal(size = k, loc = mus[i], scale = sigs[i])
                        ns = np.repeat(i,k)
                        df = pd.DataFrame({'label':ns,'vars':dist1})
                        dfALL = pd.concat([dfALL,df])


                    train_x, test_x, train_y, test_y = train_test_split(dfALL['vars'], dfALL['label'],train_size=0.7, stratify = dfALL['label'])
                    train_y = train_y.astype('int')
                    test_y = test_y.astype('int')
                    test_x = test_x.reshape(-1,1)
                    train_x = train_x.reshape(-1,1)
                    LogReg = LogisticRegression()
                    #LogReg = LogisticRegression(class_weight = 'balanced')
                    y_pred = LogReg.fit(train_x, train_y)
                    y_pred = LogReg.predict(test_x)
                    y_predp = LogReg.predict_proba(test_x)
                    cm = metrics.confusion_matrix(test_y, y_pred)
                    auc = metrics.roc_auc_score(test_y,y_pred)
                    roc = metrics.roc_curve(test_y,y_pred)
                    d = {"auc": auc, "TP":cm[0][0]/n, "FP":cm[0][1]/n,"FN":cm[1][0]/n,"TN":cm[1][1]/n, "Pos Prop": proportion[0]/sum(proportion),
                    "n": n, "mu1": mus[0], "mu2": mus[1], "deltamu": mus[1]- mus[0],"sig1": sigs[0],"sig2": sigs[1], "deltasig":sigs[1]-sigs[0],
                    "effectsize":(mus[1]- mus[0])/np.std(dfALL['vars']), "pospred": (cm[0][0] + cm[1][0])/n}
                    writer.writerow(d)
