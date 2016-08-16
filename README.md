# ProxyHelper

[![Join the chat at https://gitter.im/Nithmr/ProxyHelper](https://badges.gitter.im/Nithmr/ProxyHelper.svg)](https://gitter.im/Nithmr/ProxyHelper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
This repository will contain the code for a **cool** application that would remove the need to use FoxyProxy and likes.

ProxyHelper is a set of utilities that you can **install and forget and it will just work!** It will automate all your proxy and tor configuration needs on linux. Meaning, you won't need to configure proxy for firefox, apt, git, etc manually, ever again.

Whether you are in AGH or CC or KBH, or your proxy is ```172.16.12.2``` or ```172.16.20.2``` or ```anything else```, all of the work is done in background and proxy is set for you as soon as you connect to the network, magically (and automatically).
Another cool thing about ProxyHelper is that it always sets the *Fastest* proxy for you. This is especially relevant if you use networks in CC or EED and you don't know which proxy will be faster -```172.16.24.2``` or ```172.16.24.3```; leave it to ProxyHelper to test both proxies and set the faster proxy automatically.
  
Also, ProxyHelper keeps your tor alive! No more **Tor has been disconnected!** messages. For details see *torpinger* file in the repository.
   
   
**Currently in Alpha, feel free to test it and report issues and bugs here. However, it is not tested for various platforms (except Kubuntu), so if you don't know how to fix a broken linux, don't install, wait for it to become stable.**  
  
===

###Supports:-
  
1. git
2. web-browsers-firefox,chrome (Set option "Use System Proxy" in preference of browser)
3. gnome proxy module
4. kde proxy module
5. apt                                 
  

===

###Requirements:-
  
**Compulsary:-**  
  
1. Linux  
2. python3+  
3. git   
  
`sudo apt-get install git`  
  
  
===  
  
**Optional:-**  
  
1. pysocks, pip3 (required only for tor related utilities)  
  
===
  
###Installation:-  

```
git clone https://github.com/Nithmr/ProxyHelper.git ~/.proxyhelper && cd ~/.proxyhelper && 
sudo chmod +x ./install.sh && ./install.sh
```  
  
Note: You may need to set proxy in git before using this.
    
===  
  
  
###Usage:- 
  
  

==== 
  
####Automatic mode 
  
This is the default behaviour. ProxyHelper automatically judges the
best proxy and sets it for you! You don't have to do anything!!


####Manual mode
  
Allows you to have more control over setting the proxy, using a simple
command line tool named "phelp". 
  
To use the manual mode, you need to enable it via:    
  
```phelp --manual```
  
To get back to auto mode, type:    
  
```phelp --auto```  
  
  
**Commands:**   
  
1. Set best proxy-  
```phelp -S```  
2. Evaluate best proxy-  
```phelp -G```  
3. Clear all proxy-  
```phelp -N```  
4. Set custom proxy-  
```phelp -C 172.16.24.2:3128``` *(Replace the proxy by what you require* 
5. Show help-    
`phelp -h`  
  

###Uninstallation
 
1. Run the uninstallation script    
  
```cd ~/.proxyhelper && sudo sh ./uninstall.sh```
