__author__ = 'slouchart'


class Action(object):

    def __init__(self, action=None):
        self.next = action

    def do(self, tape):
        if self.next is not None:
            self.next.do(tape)


class WriteTape(Action):

    def __init__(self, symbol, action=None):
        self._symbol = symbol
        Action.__init__(self, action)

    def do(self, tape):
        tape[tape.current_index] = self._symbol
        Action.do(self, tape)


class EraseTape(Action):
    def __init__(self, action=None):
        Action.__init__(self, action)

    def do(self, tape):
        tape[tape.current_index] = tape.blank
        Action.do(self, tape)


class MoveTapeLeft(Action):
    def do(self, tape):
        tape.move_left()
        Action.do(self, tape)


class MoveTapeRight(Action):
    def do(self, tape):
        tape.move_right()
        Action.do(self, tape)


class ActionFactory(object):

    @staticmethod
    def write(symbol, next):
        assert(symbol is not None)
        return WriteTape(symbol, next)

    @staticmethod
    def erase(next):
        return EraseTape(next)

    @staticmethod
    def move_left(next):
        return MoveTapeLeft(next)

    @staticmethod
    def move_right(next):
        return MoveTapeRight(next)

    @staticmethod
    def null(next):
        return Action(next)

    @staticmethod
    def create_action(action, symbol=None, next=None):
        if action == 'write':
            obj = getattr(ActionFactory, action)(symbol, next)
        else:
            obj = getattr(ActionFactory, action)(next)
        return obj


class ProgramBuilder(object):

    factory = ActionFactory

    def __init__(self):
        self._transition_table = {}

    def add_step(self, initial_state, symbol, action1, symbol1, action2, final_state):
        transition_key = (initial_state, symbol)
        transition_actions = list()

        actions = ProgramBuilder.factory.create_action(action1, symbol1)
        actions.next = ProgramBuilder.factory.create_action(action2)

        transition_actions.append(actions)
        transition_actions.append(final_state)
        self._transition_table[transition_key] = transition_actions

    def get_transition_table(self):
        return self._transition_table