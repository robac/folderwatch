#!/bin/bash

while true; do
    read -p "Do you wish to remove folderwatch? [y/n] " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

sudo systemctl stop folderwatch 
sudo systemctl disable folderwatch 
sudo rm -f /etc/folderwatch
sudo rm -f /usr/local/bin/folderwatch
sudo rm -f /etc/systemd/system/folderwatch.service
