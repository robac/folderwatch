#!/bin/bash

base_dir="$( cd "$(dirname "$0")/../.." ; pwd -P )"

while true; do
    read -p "Do you wish to install this program? [y/n] " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

sudo apt install python-yaml python-mysqldb inotify-tools
sudo mkdir /etc/folderwatch
sudo ln -s "$base_dir/conf/folderwatch.conf" /etc/folderwatch
sudo ln -s "$base_dir/bin/folderwatch" /usr/local/bin
sudo chmod +x "$base_dir/bin/folderwatch/folderwatch.sh"

