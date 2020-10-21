#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

statistics extraction for each file in datadir based on polygons in shapefile
Call 'python run_stat.py shapefile datadir attributefile'
with:
    - shapefile with polygons to extract information of
    - datadir the directory where rasterfiles are stored of which data will be extracted
    - attributes: a csv file with the class of each polygon in the shapefile

author: Finnish Geospatial Research Institute, Samantha Wittke
last update: 20.10.2020

"""

import sys
import os
import glob
import statisticscomputer
import shapeobject
import functions as fcts
import pandas as pd

theshape = sys.argv[1]
shapeobj = shapeobject.ShapeObject(theshape)
datadir = sys.argv[2]
attributes = sys.argv[3]
year = sys.argv[4]

fulldf = None

for tifpath in glob.glob(os.path.join(datadir,'*.tif')):
    statfile = statisticscomputer.StatisticsComputer(shapeobj,tifpath).statpathname
    fulldf = fcts.stat_csv(statfile, fulldf)
    #print(fulldf.columns)
    #print(fulldf.head(5))
    #fulldf = fulldf.astype({'parcelID': 'str'})
    
outname = os.path.join(os.path.split(statfile)[0], 's1_all_' + str(year) + '.csv')
dfa = pd.read_csv(attributes)
dfa = dfa.astype({'parcelID': 'str'})
#each parcelID gets its year added to the parcelID (year_parcelID)
dfa['parcelID'] = dfa['parcelID'].apply(lambda x: "{}{}{}".format(year,'_', x))
#print(dfa.columns)
print(dfa.head(5))
dfauv = pd.merge(fulldf,dfa, on='parcelID' )
print(dfauv.head(5))
dfauv.to_csv(outname, index=False)