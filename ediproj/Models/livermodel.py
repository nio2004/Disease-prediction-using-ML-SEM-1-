import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import svm

liver_dataset = pd.read_csv('D:/NISHANT/SRC/Django/ediproj/Models/indian_liver_patient.csv')
liver_dataset['Gender'] = liver_dataset['Gender'].replace({'Male': 0})
liver_dataset['Gender'] = liver_dataset['Gender'].replace({'Female': 1})
liver_dataset.to_csv('D:/NISHANT/SRC/Django/ediproj/Models/indian_liver_patient.csv', index=False)
#liver_dataset['Gender'] = liver_dataset['Gender'].map({"Male":0,"Female":1}) 

X = liver_dataset.drop(['Dataset'], axis=1)
Y = liver_dataset['Dataset']


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2)
#X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size = 0.2)

classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Accuracy score of the training data : ', training_data_accuracy)
