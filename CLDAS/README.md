## User experience

Download the data from [here](https://data.cma.cn/data/cdcdetail/dataCode/NAFP_CLDAS2.0_NRT.html)

>[!CAUTION]
> Due to the data policy of China Meteorological Data Service Center, real-name user account is only allowed to download data size less than 500MB per day. And the platform only supports time ranges of two days per query.

## Example

1. You select the time range, spatial range, and variables you want to download.
2. Then the platform will return a list of data files that match your criteria.
3. You can select the files you want to download and click the `buy` button.
5. Waiting for the download to complete, you can find a pure text containing AWS S3 links to the data files in your email inbox.
6. (optional) if you have multiple text files, you can merge them into one file using the command line:
```bash
cat *.txt > merge.txt
```
7. Finally, you can use `wget` to download the data files from the AWS S3 links in the text file:
```bash
wget -i merge.txt
```