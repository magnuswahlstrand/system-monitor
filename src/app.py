import random
from flask import Flask

INITIAL_INDEX = 0
N_INDICES = 5

app = Flask(__name__)


@app.route('/state')
def state():
    current_state = random.randint(0, N_INDICES - 1)

    return str(current_state)


if __name__ == '__main__':
    app.run(debug=True)
