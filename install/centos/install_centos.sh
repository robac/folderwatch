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
sudo ln -s "$base_dir/src/etc/folderwatch" /etc
sudo ln -s "$base_dir/src/bin/folderwatch" /usr/local/bin
sudo ln -s "$base_dir/src/systemd/folderwatch.service" /etc/systemd/system/
sudo chmod +x "$base_dir/src/bin/folderwatch/folderwatch.sh"

