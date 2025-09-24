# climate data acquisition
>[!NOTE]
> **One golden observation is worth a thousand simulations**
> - from the _Ten Extra Commandments for Climate Modeling_ by J.E. Kutzbach[^1]

## Reanalysis data
For the description of reanalysis, please find releveant literatures or blogs. 

### ERA5

For me, there are two primary kinds of ERA5 data to use for driving atmospheric model:
1. [ERA5 hourly data on pressure levels](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=overview)
2. [ERA5 hourly data on single levels](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview)

Find my experiences of downloading ERA5 data in [here](./ERA5/How_to_download_ERA5_dataset.md)

### FNL 

For me, there are two primary kinds of FNL data to use for research:

1. [NCEP FNL Operational Model Global Tropospheric Analyses, continuing from July 1999](https://gdex.ucar.edu/datasets/d083002/)
2. [NCEP GDAS/FNL 0.25 Degree Global Tropospheric Analyses and Forecast Grids](https://gdex.ucar.edu/datasets/d083003/)

>[!NOTE] GDAS has short temporal coverage than FNL but higher resolution (0.25deg vs 1deg). Besides, GDAS have both analysis and forecasts grids while FNL only have analysis product. Both of them share same temporal resolution with 6 hours. 

We can access the most complete and accurate data using gdex archiver. "Real-­time" users can get the FNL analysis grids directly from NCEP's NOMADS server, http://nomads.ncep.noaa.gov/.



## references 
[^1]: https://climatedataguide.ucar.edu/
