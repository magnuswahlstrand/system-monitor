from builtin_stategetters import BaseStateGetter


# Simply shows the second state all the time, quite boring
class BoringUserMadeStateGetter(BaseStateGetter):

    def get_state(self):
        return self.states[1]
