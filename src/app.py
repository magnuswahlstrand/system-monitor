import random
from flask import Flask

INITIAL_INDEX = 0
N_INDICES = 5

STATES = ["deploying",
          "deploying_complete",
          "testing",
          "testing_complete",
          "idle"]

app = Flask(__name__)


@app.route('/state')
def state():
    current_state = random.choice(STATES)
    return current_state

if __name__ == '__main__':
    app.run(debug=True)
