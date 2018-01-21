import sys
import yaml
import requests
import time
from flask import Flask, redirect, render_template, request, json

app = Flask(__name__)


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
    return render_template('index.html', options=options, states=possible_states)


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


# BaseGetter, should be inherited by custom plugins
# The method get_states should return any of the states defined in config.yaml
#
#
#

class BaseStateGetter:

    def __init__(self, states, options):
        self.states = states
        self.options = options

    def get_state(self):
        raise NotImplementedError("This method need to be overridden by the baseclass")


class AutomaticToggleGetter(BaseStateGetter):

    def get_state(self):
        current_index = int(time.time() * 1) % 5
        state = possible_states[current_index]
    #    state = random.choice(possible_states)

    #    if random.randint(0, 1) == 0:
    #        raise requests.RequestException("Very serious error, dude")

        return state


def read_configuration():

    with open('config.yaml', 'r') as f:
        configuration = yaml.load(f)

        options = configuration['options']
        possible_states = [add_metadata(state) for state in configuration['states']]
        # print(yaml.dump(possible_states, default_flow_style=False))
        return possible_states, options

    print("Something went wrong when reading configuration")
    sys.exit(1)


if __name__ == '__main__':

    # Read configuration from file
    possible_states, options = read_configuration()
    state_getter = AutomaticToggleGetter(states=possible_states, options=options)

    app.run(debug=True)
