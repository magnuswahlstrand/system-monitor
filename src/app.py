import random
import yaml
import requests
import time
from flask import Flask, redirect, render_template, request, json, jsonify

INITIAL_INDEX = 0
N_INDICES = 5


app = Flask(__name__)


def get_state():
    current_index = int(time.time() * 1) % 5
    state = possible_states[current_index]
#    state = random.choice(possible_states)

#    if random.randint(0, 1) == 0:
#        raise requests.RequestException("Very serious error, dude")

    return state


@app.errorhandler(requests.RequestException)
def handle_invalid_usage(error):
    return error.message, 404


@app.route('/state')
def state():

    current_state = get_state()

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

possible_states = None
options = None
if __name__ == '__main__':

    # Read configuration from file
    with open('config.yaml', 'r') as f:
        configuration = yaml.load(f)

        options = configuration['options']
        possible_states = [add_metadata(state) for state in configuration['states']]
        print(yaml.dump(possible_states, default_flow_style=False))






    app.run(debug=True)
