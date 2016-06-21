# ProxyHelper

[![Join the chat at https://gitter.im/Nithmr/ProxyHelper](https://badges.gitter.im/Nithmr/ProxyHelper.svg)](https://gitter.im/Nithmr/ProxyHelper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
This repository will contain the code for a **cool** application that would remove the need to use FoxyProxy and likes.

Parallel pinging, auto-proxy set, pinging throuh
Pings multiple proxies in parallel and sets the fastest one for you!!

###  CURRENTLY IN ALPHA. FEEL FREE TO TRY IT AND REPORT ISSUES HERE :)

####Installing is easy (Requires - linux, git)
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
