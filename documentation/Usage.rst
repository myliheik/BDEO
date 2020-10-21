Usage
=======

This page describes the usage of the provided codes. Please first read the Preparation!
Since cropspecies etc, changes over the years, please process one year at a time to fit shapefile and rasters together.


Inputdata
---------

See description of Inputdata in `Preparation`_
Make sure to run the code year by year.
Filenaming of the rasterfiles in datadir (one directtory per year is suggested): s1m_grd_20180411-20180421_mean_VV_R20m_xx.tif (important here that the year can be found at position 2 when splitting the filename by underscores and the polarization at position 4). 

Running the code
-----------------

1. ``python run_stat.py shapefile datadir attributes year``

 | with

 * shapefile: the shapefile with polygons of which statistics are to be extracted
 * datadir: the directory where the S1 mosaic tifs are stored
 * attributes: an attribute file, where the target variables are stored
 * year of the files processed

2. ``python run_ml.py csvfile sampling``

 | with

 * csvfile: one of the resulting csv files from above (parcelID and mean_polarization for all files that were in datadir (eg.: s1_all_2018.csv))
 * sampling: sampling method, one of the following (see also `imblearn <https://imbalanced-learn.readthedocs.io/en/stable/user_guide.html>`):
  * **ROS**: random over sampling
  * **RUS**: random under sampling
  * **ADASYN**: Adaptive Synthetic (over) sampling
  * **SMOTE**: Synthetic Minority Oversampling Technique
  * **CC**: Cluster Centroids (under) sampling

What is happening
------------------

1. run_stat.py

 * per polygon mean (and others, but mean is returned) is extracted from the S1 tif file with `rasterstats <https://github.com/perrygeo/python-rasterstats>` package and results are written into csv file.
 * csv file is saved into a statistics directory in the parentdirectory of the datadir with name tifname_shapename_statistics.csv and the results together with the target variable is saved into same directory with name s1_all_year.csv. The latter is the file used for the next step.

2. run_ml.py

 * the above created csv file is further prepared for machine learning
 * the code runs automatically `random forest (sklearn) <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>` , `xgboost <https://xgboost.readthedocs.io/en/latest/python/python_intro.html>` and `logistic regression <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html>` with default parameters, saves the predicted targets (overrides existing files with same name (classifier_pred.csv)) for each and writes several performance metrics on screen. 





