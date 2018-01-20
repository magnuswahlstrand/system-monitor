import random
import yaml
import json
from flask import Flask

INITIAL_INDEX = 0
N_INDICES = 5


app = Flask(__name__)


@app.route('/state')
def state():

    if STATES:
        current_state = random.choice(STATES)
    else:
        current_state = "unknown"
    return json.dumps(current_state)


STATES = None
if __name__ == '__main__':

    # Read configuration from file
    with open('config.yaml', 'r') as f:
        configuration = yaml.load(f)
        STATES = configuration['states']

    # Help to generate more advanced yamls
    # print(yaml.dump({'states':STATES}, default_flow_style=False))

    app.run(debug=True)
