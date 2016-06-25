#!/bin/bash

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
	echo 'This script should be run with root permission'
	exit
fi

cd ~/.proxyhelper
git pull origin master

