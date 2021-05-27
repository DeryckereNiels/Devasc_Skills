#!/bin/bash

FILES=~/labs/devnet-src/Devasc_Skills/ios_configs/*.txt
touch check_ios.rep

echo $(date) >> check_ios.rep
echo " " >> check_ios.rep
echo "STARTING IOS CHECK">>check_ios.rep
for f in $FILES 
do


 cat $f |grep hostname >>check_ios.rep
 echo "This device need upgrading" >>check_ios.rep
 echo  " " >>check_ios.rep
done
cat check_ios.rep
