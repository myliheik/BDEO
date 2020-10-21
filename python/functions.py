#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

functions for the use in bigdataEO project, used by run_ml.py and run_stat.py
see function comments for short description

author: Finnish Geospatial Research Institute, Samantha Wittke
last update: 19.10.2020

"""
import os
import pandas as pd 
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.under_sampling import ClusterCentroids
from imblearn.under_sampling import RandomUnderSampler

from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
from sklearn.linear_model import LogisticRegression

from sklearn import metrics
import numpy as np


#reads csv with statistics per field parcel and returns prepared dataframe
def stat_csv(statfile, fulldf):

    df = pd.read_csv(statfile)
    name = os.path.split(statfile)[-1]
    meandf = df[['parcelID','mean']]
    year = name.split('_')[2][:4]
    pol = name.split('_')[4]
    meandf.rename(columns={'parcelID':'parcelID','mean':'mean_'+ pol},inplace=True)
    meandf = meandf.astype({'parcelID': 'int'})
    print(meandf.head())
    meandf['parcelID'] = meandf['parcelID'].apply(lambda x: "{}{}{}".format(year,'_', x))
    
    #print(fulldf.shape)
    if fulldf is None:
        fulldf = meandf
    else:
        fulldf= pd.merge(fulldf,meandf, on='parcelID')
    print(fulldf.shape)
    print(fulldf.head())
    return fulldf

#normalization and train/test split of data from csv, in preparation for ml
def prep_data_ml(csv, yearbool = False, year = None):

    ## create dataframe and prepare for ML

    df = pd.read_csv(csv)
    #print(df)

    if yearbool:
        df['year'] = df['parcelID'[0:4]]

        #choose which dataset to use (if multiple years are in same dataset)
        df = df.loc[df['year']== str(year)]

    #choose which dataset to use (if multiple types are in same dataset), drops all other columns than mentioned
    #df = df.filter([mode, 'target'])
    df = df.drop(columns=['parcelID'])
    #df = df.dropna(axis = 0, how = 'any')
    #print(df)
    #df.set_index('parcelID', inplace=True)
    target = df['target']

    if yearbool:
        data = df.drop(columns=['target','year'])
    
    datanow = df.drop(columns=['target'])
    print(datanow)
    col = datanow.columns

    #normalize the dataset
    data = preprocessing.normalize(datanow)

    #splitting to train and test-set

    X_train, X_test, y_train, y_test = train_test_split(data,target, test_size=0.3)

    return X_train, X_test, y_train, y_test, col

#sampling of training set, according to user input, returns sampled training set
def sampling(X_train, y_train, smpl):

    if smpl == 'ROS':
        ros = RandomOverSampler(random_state=0)
        X_train, y_train = ros.fit_resample(X_train, y_train)

    elif smpl == 'SMOTE':
        X_train, y_train = SMOTE().fit_resample(X_train, y_train)

    elif smpl == 'ADASYN':
        X_train, y_train = ADASYN().fit_resample(X_train, y_train)

    elif smpl == 'CC':
        cc = ClusterCentroids(random_state=0)
        X_train, y_train = cc.fit_resample(X_train, y_train)

    elif smpl == 'RUS':
        rus = RandomUnderSampler(random_state=0)
        X_train, y_train = rus.fit_resample(X_train, y_train)

    return X_train, y_train

##Classifiers

#Random Forest
def rf(X_train,y_train,X_test, col):
    clf=RandomForestClassifier(n_estimators=100, class_weight='balanced')
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)

    feature_imp = pd.Series(clf.feature_importances_, index= col).sort_values(ascending=False)
    print(feature_imp)

    return y_pred


#XGBOOST
#https://www.datacamp.com/community/tutorials/xgboost-in-python

def xgbf(X_train,y_train,X_test, y_test):
    DM_train = xgb.DMatrix(data = X_train, label = y_train)  
    DM_test = xgb.DMatrix(data = X_test, label = y_test)
    xg_reg = xgb.XGBClassifier(objective ='binary:logistic', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)
    xg_reg.fit(X_train,y_train)
    y_pred = xg_reg.predict(X_test)

    return y_pred


#log regression
#https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html

def lr(X_train,y_train,X_test):
    clf = LogisticRegression(random_state=0, multi_class = 'multinomial',solver = 'lbfgs').fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    return y_pred


#performance evaluation
#https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics

def print_perf(y_test,y_pred):

    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print('Confusion Matrix')
    print(metrics.confusion_matrix(y_test, y_pred))
    print('Classification Report')
    print(metrics.classification_report(y_test, y_pred))
    rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    print("RMSE: %f" % (rmse))
    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred, pos_label=2)
    print(metrics.auc(fpr, tpr))

