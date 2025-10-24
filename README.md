# climate data acquisition
>[!NOTE]
> **One golden observation is worth a thousand simulations**
> - from the _Ten Extra Commandments for Climate Modeling_ by J.E. Kutzbach[^1]

## Reanalysis data
For the description of reanalysis, please find releveant literatures or blogs. 

### 1. ERA5

For me, there are two primary kinds of ERA5 data to use for driving atmospheric model:
1. [ERA5 hourly data on pressure levels](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=overview)
2. [ERA5 hourly data on single levels](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

Find my experiences of downloading ERA5 data in [here](./ERA5/How_to_download_ERA5_dataset.md)

### 2. FNL 

For me, there are two primary kinds of FNL data to use for research:

1. [NCEP FNL Operational Model Global Tropospheric Analyses, continuing from July 1999](https://gdex.ucar.edu/datasets/d083002/)
2. [NCEP GDAS/FNL 0.25 Degree Global Tropospheric Analyses and Forecast Grids](https://gdex.ucar.edu/datasets/d083003/)

>[!CAUTION]
>GDAS has short temporal coverage than FNL but higher resolution (0.25deg vs 1deg). Besides, GDAS have both analysis and forecasts grids while FNL only have analysis product. Both of them share same temporal resolution with 6 hours. 

We can access the most complete and accurate data using gdex archiver. "Real-­time" users can get the FNL analysis grids directly from NCEP's NOMADS server, http://nomads.ncep.noaa.gov/.

## Radiosondes 

### 1. [University of Wyoming Atmospheric Science Radiosonde Archive](https://weather.uwyo.edu/upperair/sounding.shtml)

Apparently, user could click required station and date to download data through web UI. However, it is not convenient to download data for multiple stations and dates. Therefore, I check the source code of the website and find that the website use JSON to store the [station info](./uwyo/stations.json). Through requesting the JSON info and filtering the stations, we can download the data for multiple stations and dates. More details could be find [here](./uwyo/download_uwyo_sounding.py)

## Analysis 

### 1. CMA Land Data Assmilation System (CLDAS)

We can access this dataset via [official website](https://data.cma.cn/data/cdcdetail/dataCode/NAFP_CLDAS2.0_NRT.html) and registered account of China Meteorological Data Service Center/National Meteorological Information centre.

This dataset have two variants: real time product and near real time product. Both of them share almost same information according to official dataset. (e.g., same temporal-spatial resolution of $0.0625^o$ and hourly, covering east Asia ($0-65^oN$, $60-160^oE$) ).

## references 
[^1]: https://climatedataguide.ucar.edu/
