# IVAOWrapper
Light Python 3 Wrapper for IVAO Network   [![Pyversions](https://img.shields.io/pypi/pyversions/IVAOWrapper?style=flat-square)](https://pypi.python.org/pypi/IVAOWrapper)

## Install and use
 * Simply run ``pip install IVAOWrapper``
 * Basic structure : 
 ```
from ivao import Server

server = Server()

# You event handlers go here 

server.run_update_stream(delay=4)
``` 

### Examples 
 * Examples can be found the the [example.py](https://github.com/Tchekda/IVAOWrapper/blob/dev/example.py) file
 * Some personal scripts are located [Tchekda/IVAO-Utils](https://github.com/Tchekda/IVAO-Utils)


## Build
 - Master : [![Build Status](https://travis-ci.com/Tchekda/IVAOWrapper.svg?branch=master)](https://travis-ci.com/Tchekda/IVAOWrapper)
 - Dev :  [![Build Status](https://travis-ci.com/Tchekda/IVAOWrapper.svg?branch=dev)](https://travis-ci.com/Tchekda/IVAOWrapper)

You are free to open an issue if you have a problem, and welcome to make a PR to improve the wrapper

Tested with some versions of Python, might work with newer ones.
### Dev Requirements
 - `requests` to grab whazzup file
 - `pdoc3` to generate html documentation


## Events List
 * `update` : When new data is parsed, given with clients list
 * `connect` : When a client connects to the network, given with client type object
 * `disconnect` : When a client disconnects from the network, given with client type object
 * `atis_update` : When an ATC updates ATIS, given with ATC object
 * `takeoff` : When a pilot takeoff, given with pilot object
 * `land` : When a pilot lands, given with pilot object
 * `static` : When pilot's position didn't changed since last update, given with pilot object
 * `moving` : When pilot's position changed since last update, given with pilot object
 
 Further documentation can be found in the [docs](https://tchekda.github.io/IVAOWrapper/)
 