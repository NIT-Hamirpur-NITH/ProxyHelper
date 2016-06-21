# ProxyHelper

[![Join the chat at https://gitter.im/Nithmr/ProxyHelper](https://badges.gitter.im/Nithmr/ProxyHelper.svg)](https://gitter.im/Nithmr/ProxyHelper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
This repository will contain the code for a **cool** application that would remove the need to use FoxyProxy and likes.

ProxyHelper is a set of utilities that you can **install and forget and it will just work!** It will automate all your proxy and tor configuration needs on linux. Meaning, you won't need to configure proxy for firefox, apt, git, etc manually, ever again.

Whether you are in AGH or CC or KBH, or your proxy is ```172.16.12.2``` or ```172.16.20.2``` or ```anything else```, all of the work is done in background and proxy is set for you as soon as you connect to the network, magically (and automatically).
Another cool thing about ProxyHelper is that it always sets the *Fastest* proxy for you. This is especially relevant if you use networks in CC or EED and you don't know which proxy will be faster -```172.16.24.2``` or ```172.16.24.3```; leave it to ProxyHelper to test both proxies and set the faster proxy automatically.
  
Also, did I mention with ProxyHelper you can use internet with *tor* even after 2 A.M limit?(potentially to the next day!).   
Yes ProxyHelper can do it and has many more intereting feature which are discussed below. (see **More Features**)  
 
**Currently in Alpha, feel free to test it and report issues and bugs here.**  
  
  
  
===
###Installation

```
1) Clone the directory
2) cd ProxyHelper
3) chmod +x install.sh
4) sudo ./install.sh
```
###How to know if it's working?


To reset the proxy ( Pass a **None** argument )
```
sudo ./zetproxy None
```

Mostly not required ( nor recommended )

##### To edit the proxy pool
```
1) Open surely_parallel.py in your favorite text editor
2) Look for the *proxies* list near the top
3) Add/Remove proxy from the list 
```
