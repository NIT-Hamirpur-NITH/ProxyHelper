# ProxyHelper

[![Join the chat at https://gitter.im/Nithmr/ProxyHelper](https://badges.gitter.im/Nithmr/ProxyHelper.svg)](https://gitter.im/Nithmr/ProxyHelper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
This repository will contain the code for a **cool** application that would remove the need to use FoxyProxy and likes.

ProxyHelper is a set of utilities that you can **install and forget and it will just work!** It will automate all your proxy and tor configuration needs on linux. Meaning, you won't need to configure proxy for firefox, apt, git, etc manually, ever again.

Whether you are in AGH or CC or KBH, or your proxy is ```172.16.12.2``` or ```172.16.20.2``` or ```anything else```, all of the work is done in background and proxy is set for you as soon as you connect to the network, magically (and automatically).
Another cool thing about ProxyHelper is that it always sets the *Fastest* proxy for you. This is especially relevant if you use networks in CC or EED and you don't know which proxy will be faster -```172.16.24.2``` or ```172.16.24.3```; leave it to ProxyHelper to test both proxies and set the faster proxy automatically.
  
Also, ProxyHelper keeps your tor alive! No more **Tor has been disconnected!** messages. For details see *torpinger* file in the repository.
   
   
**Currently in Alpha, feel free to test it and report issues and bugs here. However, it is not tested for various platforms (except Kubuntu), so if you don't know how to fix a broken linux, don't install, wait for it to become stable.**  
  
===

###More Features
  
This section is yet to be written. It will contain an in-depth description of the components of ProxyHelper  

===

###Requirements:-
  
1. **Linux**  -  ProxyHelper doesn't support for windows unfortunately (Yet)  
2. **Git**  -  You need to have git installed in your system   
```sudo apt-get install git```  
3. **Python3**  -  In Ubuntu based distributions since 14.04 it is already installed, otherwise you need to install this by yourself.   

The below are required only if you want to use **tor** related utilities:-
  
4. **pip-3**  -  Again, this should come already installed with your OS, otherwise follow the step below.  
```sudo apt-get install python3-pip```
5. **socks python module**   
```sudo -H pip3 install pysocks```

===

###Installation  
1. Clone the repository to your machine home directory with the below command   
```git clone https://github.com/Nithmr/ProxyHelper ~/.proxyhelper```
2. Move to the directory "~/.proxyhelper" by   
```cd ~/.proxyhelper```
3. Make the installer script executable  
```chmod +x install.sh```  
4. Run the installer script  
```sudo ./install.sh```
    
===


###How to know if ProxyHelper is working?   

You may need to restart you terminal for this. Also, reconnect your interent connection to see ProxyHelper perform it's auto-proxy-set feature.    
  
1. You should be able to execute torpinger and zetproxy as a command in the shell. Type :-    
```zetproxy ```  
or      
```torpinger ```
3. Check the content of /var/tmp/torpingtest in interval of some time, if some lines are being added to the file automatically, then voila! your torpinging is working perfectly fine    
```cat /var/tmp/torpingtest ```
4. Check the content of your /etc/environment file, the best proxy for your network should be automatically set there.    
```cat /etc/environment ```

===


###Uninstallation
  
1. Go to the directory where you cloned ProxyHelper  
```cd ~/.proxyhelper```
2. Run the uninstallation script  
```sudo ./uninstall.sh```
   
===

###To reset the proxy  
1. Go to the directory where you cloned ProxyHelper  
2. Type the line below in the shell  
```sudo ./zetproxy None```

===
