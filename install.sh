#!/bin/sh

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
	echo 'This script should be run with root permission'
	exit
fi

chmod +x ./zetproxy
mv ./zetproxy /etc/network/if-up.d
mv ./surely_parallel.py /etc/network/if-up.d

