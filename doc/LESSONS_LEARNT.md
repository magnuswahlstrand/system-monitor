# Lessons learnt (Not user documentation)

### Reading configuration
It is much easier to handle missing configuration in data in backend, rather than in the jinja2 templates sida.

### Really cool graphs
http://formidable.com/open-source/victory/gallery/animating-circular-progress-bar/


### Reading configuration from Python
ConfigParser, YAML, or JSON

https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file

#### Read all options for a section
```python
dict(Config.items('Section'))
```


# YAML
```python
print(yaml.dump({'states':STATES}, default_flow_style=False))
```


# Handling exceptions in Flask (nice!)
```python
@app.errorhandler(requests.RequestException)
def handle_invalid_usage(error):
    return error.message, 404
```

# KNOBS
This is ridiculously cool. Need to be used.

https://www.cssscript.com/demo/touch-enabled-knob-control-pure-javascript-jim-knopf/

https://www.jqueryscript.net/demo/Nice-Touchable-jQuery-Dial-Plugin-Knob/