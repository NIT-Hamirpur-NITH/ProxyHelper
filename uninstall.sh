#!/bin/sh

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
    echo 'This script should be run with root permission'
    exit
fi

rm /etc/network/if-up.d/torpinger
rm /etc/network/if-up.d/zetproxy
rm /usr/bin/phelp


echo Uninstallation complete
