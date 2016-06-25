#!/bin/sh

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
    echo 'This script should be run with root permission'
    exit
fi

zetproxy None
rm /etc/network/if-up.d/torpinger
rm /etc/network/if-up.d/zetproxy
rm /usr/bin/torpinger
rm /usr/bin/zetproxy


echo Uninstallation complete
