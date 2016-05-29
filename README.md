# ProxyHelper

[![Join the chat at https://gitter.im/Nithmr/ProxyHelper](https://badges.gitter.im/Nithmr/ProxyHelper.svg)](https://gitter.im/Nithmr/ProxyHelper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
This repository will contain the code for a **cool** application that would remove the need to use FoxyProxy and likes.


Sets proxy for system based on network with which it is connected.

You can specify all proxies associated with a given network and the script
will choose the fastest between them and set it for the system.


#### To add/edit a network
```
1) Go to proxy.dbase
2) Add the network name
3) Add single space after name
4) Write all the possible proxies for network separated by space
5) If no proxy write "None"
```
#### To run the script
```
1) chmod +x setproxy.bash
2) sudo ./setproxy.bash
```
