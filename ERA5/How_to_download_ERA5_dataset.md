---
title: How to download ERA5 dataset
creation date: 2025-09-23 23:17
modification date: 2025-09-24 00:07
author: Jun Gu
---

Actually there are three kinds of download methods[^1]:

1. using web UI [ERA5 hourly data on pressure levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download) and interactively select desired variables and date. Then submit the request and waiting request finished in server side. Lastly, click the download button or copy the download link and using `wget` or `IDM` professional downloaders. 
2. using cdsapi client and python script to complete data downloading in batch.
    1. [CDSAPI setup](https://cds.climate.copernicus.eu/how-to-api)
    2. when using web UI from ERA5, it would automatically generate a python script. 
    ```python
    import cdsasi
    cdsapi.Client().retrieve(dataset, request, filename)
    ```
    3. Except that automatically generated scripts, I also write a script which could drive models [here](./ERA5/download_ERA5_dirve_MPAS.py) or multiple initial conditions [here](./ERA5/download_ERA5_drive_multi_init.py)

3. Sometimes, the ERA5 server side could be suffering from too many requests or the download speed is slow in client side. In this case, I would use an archiver named [NCAR|GDEX](https://gdex.ucar.edu/datasets/d633000/) to download ERA5 data.

Except these mainstream methods, some enterprises or cloud servers provide ERA5 data for trainning their AI models, such as [google-research/arco-era5](https://github.com/google-research/arco-era5/)


[^1]:[How to download ERA5 - Copernicus Knowledge Base - ECMWF Confluence Wiki](https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5)