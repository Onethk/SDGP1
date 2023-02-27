import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

df = pd.read_csv("Final5.csv")
# df.drop('HowYouPrepare',axis = 1, inplace = True)
# df.drop('Rate yourself',axis = 1, inplace = True)

X = df.drop("Marks",axis = 1)
y = df["Marks"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X , y , test_size = 0.3)

from sklearn.tree import DecisionTreeClassifier

decisionModel = DecisionTreeClassifier()
decisionModel.fit(X_train,y_train)

decisionPred = decisionModel.predict(X_test)


from sklearn.ensemble import RandomForestClassifier

randForestModel = RandomForestClassifier()
randForestModel.fit(X_train, y_train)

randForestPred = randForestModel.predict(X_test)

from sklearn import svm

svm_model= svm.SVC(decision_function_shape='ovo')
svm_model.fit(X_train, y_train)

svm_pred = svm_model.predict(X_test)


from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


estimators_list = [('model1',decisionModel),('model2',randForestModel),('model3',svm_model)]

pipe = make_pipeline(StandardScaler(), StackingClassifier(estimators = estimators_list, final_estimator = LogisticRegression(max_iter=2000)))
                     
pipe.fit(X_train.values, y_train)

# stackPred = pipe.predict([[1,1,3,0,0,1,1,2,1,1,1,3,1,1]])
# stackPred1 = pipe.predict([[1,1,4,0,0,3,2,2,2,1,0,3,0,2]])
# stackPred2 = pipe.predict([[1,1,4,0,0,3,2,2,2,1,0,3,0,2]])


# stackPred
    
# print(stackPred)
# print(stackPred1)

import pickle

with open('model_pickle_final.h5','wb') as f:
    pickle.dump(pipe,f)
    
