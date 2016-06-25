#!/bin/sh

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
	echo 'This script should be run with root permission'
	exit
fi

if [ ! $(pwd | sed 's/\/.*\/.*\///') = '.proxyhelper' ]
then
    echo You are not in ~/.proxyhelper directory, you are doing it wrong
    echo See steps on github.com again
    exit
fi


chmod +x ./zetproxy
chmod +x ./torpinger
chmod +x ./auto-update.sh
chmod +x ./uninstall.sh

ln -s zetproxy /usr/bin/
ln -s zetproxy /etc/network/if-up.d/
ln -s torpinger /usr/bin/
ln -s torpinger /etc/network/if-up.d/
echo Created symlinks to /usr/bin/ for zetproxy and torpinger

echo Installation complete
