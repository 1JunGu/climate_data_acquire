#!/bin/bash
#see the name conventions from https://data.cma.cn/article/showPDFFile.html?file=/pic/static/doc/F/CLDAS-V2.0/CLDAS-V2.0_ADP.pdf
for i in $(ls |grep Z_NAFP);do
	echo "Processing: " $i
	#delete redundant characters after the last ?
	newfile_1=${i%%\?*}
	mv $i ${newfile_1}

	#delete prefix strings
	newfile_2=${newfile_1:29}
	mv ${newfile_1} ${newfile_2}
	echo "Processed: " ${newfile_2}
done
