
# System Monitor
The **System Monitor** is a web app that monitors the state of a system and visualizes it using *Alvaro Trivago's* excellent plugin [fullPage.js](https://alvarotrigo.com/fullPage/). 

_Example of **System Monitoring** following a simple test system_

![alt text](doc/example.gif "Example of monitoring")

While the builtin plugins (plugins/builin_stategetters.py), generates a dummy state from the defined states specified in `config.yaml`, the goal of *System Monitor* is to be easily extendable to get the state of **anything** :+1:.
Please refer to the [Add your own plugin](#guide-add-your-own-plugin) section.

## Basic Usage

1. (optional): Use virtual env 
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt 
```
2. Run start app
```bash
python app.py
```
3. Go to [localhost:5000](http://localhost:5000) to see something like this


![alt text](doc/example.gif "Example of monitoring")

## Change StateGetter
To change the plugin that parses states, open **config.yaml** and change the `stateGetter` option to one of the following
```yaml
options:
  stateGetter: plugins.builtin_stategetters.AutomaticToggleGetter
#  stateGetter: plugins.builtin_stategetters.RandomStateGetter
#  stateGetter: plugins.builtin_stategetters.BrokenRandomStateGetter
#  stateGetter: plugins.usermade_stategetter.BoringUserMadeStateGetter
```

## Plugins
### Add your own plugin
1. Create a plugin file `usermade_stategetter.py`

![alt text](doc/new_plugin.png "Path to user made stategetter" )

2. Create a class `BoringUserMadeStateGetter` that inherits `BaseStateGetter` and implements `get_state`. See [plugins/builtin_stategetters.py](plugins/builtin_stategetters.py) for examples.

**plugins/usermade_stategetter.py**
```python
from builtin_stategetters import BaseStateGetter
# Simply shows the second state all the time, quite boring
class BoringUserMadeStateGetter(BaseStateGetter):

    def get_state(self):
        return self.states[1]
```
3. Make *System Monitor* use the new plugin by updating the `config.yaml` to point to your plugin.

**config.yaml**
```yaml
options:
  stateGetter: plugins.usermade_stategetter.BoringUserMadeStateGetter
...
```


### Custom options in your own plugin
1. Add the new attribute to your `config.yaml` under options

**config.yaml**
```yaml
options:
  stateGetter:      plugins.usermade_stategetter.BoringUserMadeStateGetter
  YOUR_ATTRIBUTE:   2
...
```
2. Use the attribute `self.option['YOUR_ATTRIBUTE']` to access it in your plugin

**plugins/usermade_stategetter.py**
```python
from builtin_stategetters import BaseStateGetter
# Simply shows the second state all the time, quite boring
class BoringUserMadeStateGetter(BaseStateGetter):

    def get_state(self):
        fixed_index = int(self.options['YOUR_ATTRIBUTE'])  # Note: need to convert from string to int
        return self.states[fixed_index]
```

# Todos
#### Release 0.3
* Group pages on same row
* Read custom options in plugins
* Document how to add custom options to plugins

#### Release 0.x
* PLUGIN: REST
* PLUGIN: ElasticSearch
* Change URL from options

## Done
#### Release 0.3
* Document how to add plugins
* Move app files from src to root folder

#### Release 0.2
* ~~Record new gif~~
* ~~Choose python function based on config. [Example how to load module](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string)~~
* ~~Add plugin system~~
* ~~Handle local server down~~
* ~~Change port for local server~~
* ~~PLUGIN: Error plugin~~
* ~~PLUGIN: Progressive plugin~~