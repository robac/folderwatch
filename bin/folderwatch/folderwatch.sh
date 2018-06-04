#!/bin/bash

my_dir=`dirname $0`
command=$(python $my_dir/tftpparameters.py $1)

set -f 
echo $command
echo $my_dir
$command |
while read -r directory events filename; do
    python $my_dir/tftpbackup.py $1 $directory $events $filename
    echo "python $my_dir/tftpbackup.py $1 $directory $events $filename"
done
set +f
