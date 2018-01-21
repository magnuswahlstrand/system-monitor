

# BaseGetter, should be inherited by custom plugins
# The method get_states should return any of the states defined in config.yaml
class BaseStateGetter:

    def __init__(self, states, options):
        self.states = states
        self.options = options

    def get_state(self):
        raise NotImplementedError("This method need to be overridden by the baseclass")
