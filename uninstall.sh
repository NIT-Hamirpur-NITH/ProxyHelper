#!/bin/sh

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
    echo 'This script should be run with root permission'
    exit
fi

rm /etc/network/if-up.d/surely_parallel.py
rm /etc/network/if-up.d/torpinger.py
rm /etc/network/if-up.d/zetproxy
rm /etc/network/if-up.d/zettor


echo Uninstallation complete
