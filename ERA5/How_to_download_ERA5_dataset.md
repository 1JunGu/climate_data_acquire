---
title: 
creation date: 2025-09-23 23:17
modification date: 2025-09-24 00:07
author: Jun Gu
aliases: 
type: 
tags:
---

Actually there are two kinds of download methods[^1]:

1. using web UI [ERA5 hourly data on pressure levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download) and interactively select desired variables and date. Then submit the request and waiting request finished in server side. Lastly, click the download button or copy the download link and using `wget` or `IDM` professional downloaders. 
2. using cdsapi client and python script to complete data downloading in batch.
    1. [CDSAPI setup](https://cds.climate.copernicus.eu/how-to-api)
    2. when using web UI from ERA5, it would automatically generate a python script. 
    3. Except that


[^1]:[How to download ERA5 - Copernicus Knowledge Base - ECMWF Confluence Wiki](https://confluence.ecmwf.int/display/CKB/How+to+download+ERA5)