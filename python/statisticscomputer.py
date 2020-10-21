#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
explanation
"""

import os
import csv
from rasterstats import zonal_stats
import shapeobject


class StatisticsComputer(object):

    def __init__(self, shapeobj , raster):

        self.runProcess(raster, shapeobj)

    def runProcess(self, raster, shapeobj):
        
        self.prepareStatistics()
       
        reprojectedshape = shapeobj.checkProjection(raster).theshape
        #reprojectedshape = shapeobj.theshape

        filename = os.path.splitext(raster)[0]
        rastername = os.path.split(filename)[-1]
        rasterpath = os.path.split(filename)[0]
        projectpath = os.path.split(rasterpath)[0]
        statpath = os.path.join(projectpath,'statistics')
        
        if not os.path.exists(statpath):
            os.mkdir(statpath)
        if not os.path.exists(statpath):
            os.makedirs(statpath)
        
        self.statpathname = os.path.join(statpath,rastername + '_' + shapeobj.shpname + '_statistics')
        
        print('INFO: calculating zonal statistics for '+ raster + ' and ' + reprojectedshape)
        
        a=zonal_stats(reprojectedshape, raster, stats=self.statistics, band=1, geojson_out=True)

        #to make sure the file is empty when written for first time!
        open('%s.txt' % (self.statpathname),'w').close()
        with open ('%s.txt' % (self.statpathname),'a') as sh:
            shWriter=csv.writer(sh)
            shWriter.writerow(self.statline)
        with open ('%s.txt' % (self.statpathname),'a') as sf:
            sfWriter=csv.writer(sf)
            for x in a:
                row = []
                index=0
                while index <= len(self.statline)-1:
                    onerow = x['properties'][self.statline[index]]
                    if onerow == 0.0:
                        onerow = ''
                    row.append(onerow)
                    index += 1
                sfWriter.writerow(row)
        self.statpathname = os.path.join(statpath,rastername + '_' + shapeobj.shpname + '_statistics.txt')
        print('INFO: done with statistics')

    def prepareStatistics(self):
        
        self.statline = list(['count', 'min', 'mean', 'max', 'median', 'percentile_10', 'percentile_90', 'std'])
        self.statline[:0] = ['parcelID']
        self.statistics = ' '.join(['count', 'min', 'mean', 'max', 'median', 'percentile_10', 'percentile_90', 'std'])
