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
    return render_template('index.html', options=options)

possible_states = None
options = None
if __name__ == '__main__':

    # Read configuration from file
    with open('config.yaml', 'r') as f:
        configuration = yaml.load(f)
        possible_states = configuration['states']
        options = configuration['options']

    # Help to generate more advanced yamls
    # print(yaml.dump({'states':STATES}, default_flow_style=False))

    app.run(debug=True)
