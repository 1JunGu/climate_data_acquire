---
title: How to download IMERG data
creation date: 2026-04-24 15:01
modification date: 2026-05-06 00:07
author: Jun Gu
---

## User experience
1. IMERG data belongs to NASA GES DISC data, so user needs to register an account Earthdata. 
2. create and retrieve [Earthdata Token](https://urs.earthdata.nasa.gov/documentation/for_users/user_token) for authentication.
3. For different download methods (e.g., wget, curl, python), the way to use Earthdata Token is different. Please refer to the reference for details.
4. Through the web interface, user can search the data and generate a text file containing the download links. Then use wget or curl to download the data in batch.
    1. user can directly acquire the downlooad links after selecting time range (HDF5).
    2. for advanced uses, use could also select the spatial range to minimize the size of output (NC4).

## Reference
1. [Data Access](https://disc.gsfc.nasa.gov/information/howto?title=Data%20Access)
1. [How to Access GES DISC Data Using wget and curl](https://disc.gsfc.nasa.gov/information/howto?title=How%20to%20Access%20GES%20DISC%20Data%20Using%20wget%20and%20curl)
