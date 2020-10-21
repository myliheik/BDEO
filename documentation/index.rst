.. BigDataEO documentation master file, created by
   sphinx-quickstart on Fri Oct  9 18:31:21 2020.

BigDataEO project code
===========================================

Documentation for `this <https://github.com/myliheik/BDEO>`_ code.

This documentation describes the content and usage of the code written for the BigDataEO project by the 
Finnish Geospatial Research Institute (`FGI <https://www.maanmittauslaitos.fi/en/research/departments/remote-sensing-and-photogrammetry>`) in the National Land Survey from 2018 until 2020 as a subcontractor for the Natural Resources Institute of Finland (`LUKE <https://www.luke.fi>`_).
The project aims to estimate the winter vegetation cover of agricultural fields based on Sentinel-1 `mosaics <http://metatieto.ymparisto.fi:8080/geoportal/catalog/search/resource/details.page?uuid=%7B870D6A93-E60B-4446-A092-92C863E00AE3%7D>`_ by the Finnish Meteorological Institute (FMI).
This repository includes code to extract statistics of S1 parameters per field parcel and apply some basic machine learning models (random forest, xgboost and log regression) based on request by LUKE in 2018.
The models are left in default state, to be updated as seen fit by the user. 
MIT licensed (see license file in the repository).

Contents:

.. toctree::
   :maxdepth: 2

   Preparation
   Usage
 
