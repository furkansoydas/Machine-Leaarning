# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:40:42 2019

@author: Furkan
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv("data-csv.csv")

X = dataset.iloc[:,0:2].values
y = dataset.iloc[:,2].values.reshape(-1,1)
#%%
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X = ss.fit_transform(X)

#%%

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=0)
#%%
from sklearn import tree

dtree = tree.DecisionTreeClassifier(criterion = 'entropy',random_state = 0)
dtree.fit(X_train,y_train)

#%%
from sklearn import metrics
print("Train-Accuracy :",metrics.accuracy_score(y_train,dtree.predict(X_train)))
print("-----------------------------------------------")
print("Train-Confusion:\n",metrics.confusion_matrix(y_train,dtree.predict(X_train)))
print("-----------------------------------------------")
print("Train-Classification report :",metrics.classification_report(y_train,dtree.predict(X_train)))
print("-----------------------------------------------")
print("\n")
#%%
print("Test-Accuracy :",metrics.accuracy_score(y_test,dtree.predict(X_test)))
print("-----------------------------------------------")
print("Test-Confusion:\n",metrics.confusion_matrix(y_test,dtree.predict(X_test)))
print("-----------------------------------------------")
print("Test-Classification report :",metrics.classification_report(y_test,dtree.predict(X_test)))
print("-----------------------------------------------")