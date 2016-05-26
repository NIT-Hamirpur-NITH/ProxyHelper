#!/bin/bash

# exit if not root
if [ ! $(id -u) -eq 0 ]
then
	echo 'This script should be run with root permission'
	exit
fi

# variables for protocols
hp=http_proxy
hsp=https_proxy
fp=ftp_proxy
np=no_proxy


# function to set proxy in enviroment file
proxy_env()
{
	echo "SETTING ENV PROXY"
	# if None proxy then this next line is enough
	# pipe is in extended regular expr, reqs -r to enable it in GNU sed
	sed -r "/($hp|$hsp|$fp|$np).*/d" /etc/environment >> ./.temp_file_env;
	if [ ! $WIFI_PROXY = "None" ]
	then 

		HTP=http://$WIFI_PROXY/
		HTPS=https://$WIFI_PROXY/
		FP=ftp://$WIFI_PROXY/

		printf "$hp=\"$HTP\"\n$hsp=\"$HTPS\"\n$fp=\"$FP\"\n$np=\"localhost,127.0.0.1\"\n"  >> ./.temp_file_env;
	fi
	mv ./.temp_file_env /etc/environment
}
	
# setting proxy for apt in file apt.conf
proxy_apt()
{
	echo "SETTING PROXY FOR APT, MAYBE NOT REQD FOR UBUNTU\nNECESSARY FOR KUBUNTU,XUBUNTU,LINUX MINT"
	
	# rm /etc/apt/apt.conf

	if [ $WIFI_PROXY = "None" ]
	then 
		echo clearing 95proxies file 
		printf "Acquire::http::Proxy \"false\";" >> ./.temp_file_apt;
	else

		printf "Acquire::http::Proxy \"$HTP\";\nAcquire::https::Proxy \"$HTPS\";\nAcquire::ftp::Proxy \"$FP\";\n" >> ./.temp_file_apt;
		echo creating apt.conf file	
	fi
	mv ./.temp_file_apt /etc/apt/apt.conf
}

ping_prox()
{
    echo Pinging proxy $proxy
    op=$(ping -c2 -w2 $proxy | tail -1 | sed 's/\(.*\)= //')
    echo $op
    # op is of the form min/avg/max/mdev
    # at the moment I am using only avg arg for comparison
    avg=$(echo $op | sed 's/\(.*\)\/\(.*\)\/\(.*\)\/\(.*\).*/\2/')
}

best_proxy_get()
{
    # BEST_PROX stores the proxy with lowest avg resp time
    # best_avg stores the least avg resp time found
    
    # For testing set the var as below, ie uncomment next line
    # WIFI_PROXIES="google.com bing.com wikipedia.com"
    # So you will get the BEST_PROX by this function
    # which unsurprisingly is google.com
    best_avg=10000
    echo 'Getting best proxy'
    for proxy in $WIFI_PROXIES
    do
        ping_prox
        if [[ ! -z $avg ]]
        then
            if [[ $(echo "$avg<$best_avg" | bc) = 1 ]]
            then
                echo New is better, changing demeanour
                best_avg=$avg
                BEST_PROX=$proxy
            fi
        fi
    done
    if [[ $best_avg = 10000 ]]
    then
        echo All your proxies suck dude, exitting
        exit 1
    else
        echo Best proxy is $BEST_PROX
    fi
}

# stores the state and name of available wifi networks
WIFI_DETAIL=$(nmcli -t -f active,NAME c)

# removes the networks whose state is not active
# regular expr might be over-inclusive down here :P
WIFI_REFINED=$(echo "$WIFI_DETAIL" | sed '/no.*/d' )


# counts the networks whose state is active
# should be 1, >1 is abnormal, and should not be 0
WIFI_COUNT=$(echo "$WIFI_REFINED" | grep -c yes)

if [ $WIFI_COUNT -eq 1 ]
then 	
	WIFI_NAME=$(echo "$WIFI_REFINED" | sed 's/yes:\(.*\)/\1/')
	echo WIFI_NAME: $WIFI_NAME 
	WIFI_PROXIES=$(sed -n "s/$WIFI_NAME \(.*\)/\1/p" ./proxy.dbase)
	echo WIFI_PROXIES: $WIFI_PROXIES

    # fucn call to determine fastest proxy if not None
    if [ $WIFI_PROXIES = "None" ]
    then
        WIFI_PROXY=None
    else
        best_proxy_get
        WIFI_PROXY=$BEST_PROX
    fi

	# func call to set proxy at different places
	proxy_env
	proxy_apt
else
	echo 'WIFI not connected or some abnormal scenario'
fi
