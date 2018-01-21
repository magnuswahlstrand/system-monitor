import time
import random
import requests


# BaseGetter, should be inherited by custom plugins
# The method get_states should return any of the states defined in config.yaml
class BaseStateGetter(object):

    def __init__(self, states, options):
        self.states = states
        self.options = options

    def get_state(self):
        raise NotImplementedError("This method need to be overridden by the baseclass")


# Changes state every second
class AutomaticToggleGetter(BaseStateGetter):

    def get_state(self):
        current_index = int(time.time()) % len(self.states)
        state = self.states[current_index]
        return state


# Gets a state at random
class RandomStateGetter(BaseStateGetter):

    def get_state(self):
        return random.choice(self.states)


# Gets a state at random, but every
class BrokenRandomStateGetter(RandomStateGetter):

    # How often it fails and throws an exception to the browser
    # FAILURE_RATE = 2, fails every other
    FAILS_ONCE_IN_THIS_MANY_TIME = 2

    def get_state(self):

        print random.randint(0, self.FAILS_ONCE_IN_THIS_MANY_TIME - 1)
        if random.randint(0, self.FAILS_ONCE_IN_THIS_MANY_TIME - 1) == 0:
            raise requests.RequestException("Very serious error, dude")

        # TODO: Should be able to use RandomStateGetter method here, but unsure of inheritance
        return random.choice(self.states)
