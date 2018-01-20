import random
import yaml
import json
from flask import Flask, redirect, render_template

INITIAL_INDEX = 0
N_INDICES = 5


app = Flask(__name__)


@app.route('/state')
def state():

    if possible_states:
        current_state = random.choice(possible_states)
    else:
        current_state = "unknown"
    return json.dumps(current_state)


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
