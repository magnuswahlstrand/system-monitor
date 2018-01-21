
# System Monitor
The **System Monitor** is a web app that monitors the state of a system and visualizes it using *Alvaro Trivago's* excellent plugin [fullPage.js](https://alvarotrigo.com/fullPage/). 

_Example of **System Monitoring** following a simple test system_

![alt text](doc/example.gif "Example of monitoring")

While the builtin plugins (plugins/builin_stategetters.py), generates a dummy state from the defined states specified in `config.yaml`, the goal of *System Monitor* is to be easily extendable to get the state of **anything** :+1:.
Please refer to the [Add your own plugin](#guide-add-your-own-plugin) section.



## Guide: Add your own plugin

1. Output any of the states specified in the config.yaml
2.


### Create a plugin file

![alt text](doc/new_plugin.png "Path to user made stategetter" )


In *my_stategetter.py*
```

```

### Use the Use the plugin
### Specify the


## Todos
#### Release 0.3
* Group pages on same row
* Document how to add plugins
* Read custom options in plugins
* Document how to add custom options to plugins
* Move app files from src to root folder

#### Release 0.x
* PLUGIN: REST
* PLUGIN: ElasticSearch
* Change URL from options

## Done
#### Release 0.3

#### Release 0.2
* ~~Record new gif~~
* ~~Choose python function based on config. [Example how to load module](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string)~~
* ~~Add plugin system~~
* ~~Handle local server down~~
* ~~Change port for local server~~
* ~~PLUGIN: Error plugin~~
* ~~PLUGIN: Progressive plugin~~