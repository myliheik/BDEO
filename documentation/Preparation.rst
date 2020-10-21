Preparation
============

Before running any of the provided codes please make sure you have followed the following preparatory steps:

Anaconda
---------


* Download and install **Anaconda** as described `here <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.htmlL>`_

* Create environment with environment.yml in the repository:

``conda env create -f environment.yml``

* every time before running the code, enter the created environment with ``conda activate bigdataeo``


Data Preparation
----------------

* Download Sentinel-1 mosaics
    * S1 mosaics of Finland are provided by the Finnish Meteorological Institute `here <http://metatieto.ymparisto.fi:8080/geoportal/catalog/search/resource/details.page?uuid=%7B870D6A93-E60B-4446-A092-92C863E00AE3%7D>`
* Shapefiles
    * Prepare shapefiles with field parcels, with minimum one field, named *parcelID* (since field parcels and their target variable changes per year, one shapefile per year is needed).
* Attributes
    * Prepare attribute .csv file with columns *parcelID* and *target* (which contains the reference class of the field parcel as integer)