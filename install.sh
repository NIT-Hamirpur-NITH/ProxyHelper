#!/bin/sh

# exit if root
if [ $(id -u) -eq 0 ]
then
	echo 'Run without sudo!!'
	exit
fi

home=$HOME

if [ ! $(pwd | sed 's/\/.*\/.*\///') = '.proxyhelper' ]
then
    echo Exiting. This script should be run from "~/.proxyhelper" directory
    exit
fi

chmod +x $home/.proxyhelper/zetproxy
chmod +x $home/.proxyhelper/proxyhelper.py
chmod +x $home/.proxyhelper/torpinger
#chmod +x ./auto-update.sh
chmod +x $home/.proxyhelper/uninstall.sh

# Remove earlier installations if they exist
# Needs for people with earlier version of PH
# Which might clash
if [ -x "$(command -v /usr/bin/phelp)" ]
then 
    sudo rm /usr/bin/phelp
fi
if [ -x "$(command -v /usr/bin/zetproxy)" ]
then
    sudo rm /usr/bin/zetproxy
fi
if [ -x "$(command -v /usr/bin/torpinger)" ]
then 
    sudo rm /usr/bin/torpinger
fi
if [ -x "$(command -v /etc/network/if-up.d/zetproxy)" ]
then
    sudo rm /etc/network/if-up.d/zetproxy
fi
if [ -x "$(command -v /etc/network/if-up.d/torpinger)" ]
then 
    sudo rm /etc/network/if-up.d/torpinger
fi
# symlinks fail if the path is not absolute
sudo ln -s $home/.proxyhelper/zetproxy /etc/network/if-up.d/
sudo ln -s $home/.proxyhelper/torpinger /etc/network/if-up.d/
sudo ln -s $home/.proxyhelper/proxyhelper.py /usr/bin/phelp
echo Installation complete
