# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:54:27 2019

@author: Furkan
"""
import pandas as pd

# Datamızı aldık
data = pd.read_csv('data-csv.csv')
#%%
# Renkleri Değişkeni (y) bir değişkene atadık
X = data.iloc[:,0:2].values
y = data.iloc[:,-1:].values

# Veri kümemizi test ve train şekinde ayırdık
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.33,random_state=0)
#%%
from sklearn.neighbors import KNeighborsClassifier

# KNeighborsClassifier sınıfından bir nesne ürettik
# n_neighbors : K değeridir. Bakılacak eleman sayısıdır. Default değeri 5'tir.
# metric : Değerler arasında uzaklık hesaplama formülüdür.

knn = KNeighborsClassifier(n_neighbors=2,metric='minkowski')
#%%
# Makineyi eğitiyoruz
knn.fit(x_train,y_train.ravel())

# Test verisi üzerinden elmaların rengini tahmin ettirdik
result = knn.predict(x_test)
#%%
# Karmaşıklık matrisi
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,result)
print(cm)
#%%
# Başarı Oranı
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, result)
print(accuracy)