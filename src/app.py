import sys
import yaml
import requests
import importlib
from flask import Flask, redirect, render_template, request, json
from plugins.builtin_stategetters import *
import logging

app = Flask(__name__)
VERSION = 0.2

@app.errorhandler(NotImplementedError)
def handle_not_implemented(error):
    return "The StateGetter plugin used has not implemented get_state() method", 500


@app.errorhandler(requests.RequestException)
def handle_invalid_usage(error):
    return error.message, 404


@app.route('/state')
def state():

    current_state = state_getter.get_state()

    response = json.dumps(current_state, sort_keys=True, indent=4, separators=(',', ': '))

    # Check if ?refresh is specified for demo, used for demo purposes
    if 'refresh' in request.args:
        response = '<meta http-equiv="refresh" content="0.5">' + response.replace('\n', '<br>').replace(" ", "&nbsp;")

    return response


@app.route('/')
def home():
    return redirect("/ui", code=302)


@app.route('/ui')
def ui():
    return render_template('index.html', options=options, states=possible_states, version=VERSION)


# Add metadata to states that only has basic configuration
def add_metadata(state_info):

    metadata = {}

    # Some metadata is defined
    if isinstance(state_info, dict):
        basename = state_info.keys()[0]
        default_text = basename.title().replace("_", " ")

        metadata['basename'] = basename
        metadata['title'] = state_info.values()[0].get('title', default_text)
        metadata['text'] = state_info.values()[0].get('text', default_text)
    else:
        basename = state_info
        default_text = basename.title().replace("_", " ")
        metadata['basename'] = basename
        metadata['title'] = default_text
        metadata['text'] = default_text

    return metadata


def read_configuration():

    with open('config.yaml', 'r') as f:
        configuration = yaml.load(f)

        options = configuration['options']
        possible_states = [add_metadata(state) for state in configuration['states']]
        # print(yaml.dump(possible_states, default_flow_style=False))

        # Verify mandatory fields exist in options
        if 'stateGetter' not in options:
            raise KeyError(""" Mandatory option 'stateGetter' missing in 'config.yaml'.

Example:

options:
  stateGetter: plugins.builtin_stategetters.RandomStateGetter
""")

        return possible_states, options


def load_getter_class(options):
    state_getter_class = options['stateGetter']
    mod_name, class_name = state_getter_class.rsplit('.', 1)
    mod = importlib.import_module(mod_name)
    getter_class = getattr(mod, class_name)
    return getter_class


if __name__ == '__main__':

    # Read configuration from file
    try:
        possible_states, options = read_configuration()
    except KeyError as e:
        logging.error(e)
        sys.exit(1)

    # Get state getter class from config file

    try:
        StateGetter = load_getter_class(options)
    except ImportError as e:
        error_msg = ". '%s' doesn't exist." % options['stateGetter'].rsplit(".", 1)[0]
        logging.error(e.message + error_msg)
        sys.exit(1)
    except AttributeError as e:
        error_msg = "Class '%s' doesn't exist." % options['stateGetter'].split(".")[-1]
        logging.error(error_msg)
        sys.exit(1)

    state_getter = StateGetter(states=possible_states, options=options)

    print(state_getter)

    app.run(debug=True)
