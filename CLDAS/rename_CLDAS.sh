#!/bin/bash
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
