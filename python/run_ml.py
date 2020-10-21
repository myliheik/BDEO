#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

author: Finnish Geospatial Research Institute, Samantha Wittke
last update: 09.10.2020

"""

import os
import sys
import functions as fcts
import pandas as pd


##read in first argument, this is the csv file with data

csv = sys.argv[1]
sampling = sys.argv[2]

# if you want yearly data set yearbool=True, and enter the year YYYY as additional arguments

X_train, X_test, y_train, y_test, col = fcts.prep_data_ml(csv)

#sampling
#ROS
#RUS
#ADASYN
#SMOTE
#CC

X_train, y_train = fcts.sampling(X_train, y_train,sampling)


# create model and predict y

y_pred_rf = fcts.rf(X_train,y_train,X_test, col)
pd.DataFrame(y_pred_rf, columns=['predictions']).to_csv('rf_pred.csv')

y_pred_xgb = fcts.xgbf(X_train,y_train,X_test, y_test)
pd.DataFrame(y_pred_xgb, columns=['predictions']).to_csv('xgb_pred.csv')

y_pred_lr = fcts.lr(X_train,y_train,X_test)
pd.DataFrame(y_pred_lr, columns=['predictions']).to_csv('lr_pred.csv')


# print performance metrics
print('random forest')
fcts.print_perf(y_test,y_pred_rf)
print('xgboost')
fcts.print_perf(y_test,y_pred_xgb)
print('logistic regression')
fcts.print_perf(y_test,y_pred_lr)


