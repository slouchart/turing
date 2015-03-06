__author__ = 'slouchart'

import tape

default_blank = '_'

class TuringMachine(object):

    def __init__(self, symbols=[], states=[], initial=0, finals=[], transitions={}, initial_input="", blank=default_blank):
        self._tape = tape.Tape(blank, initial_input)
        self.blank = blank
        self.states = states
        self.symbols = symbols
        self.initial_state = initial
        self.final_states = finals
        self.transitions = transitions
        self.current_state = initial
        self._final = False

    def run(self):
        while not self.final:
            self.step()

    @property
    def final(self):
        return self.current_state in self.final_states or self._final

    def step(self):

        transition = (self.current_state, self.read_symbol())
        if transition in self.transitions:
            action = self.transitions[transition]
            action[0].do(self._tape)
            self.current_state = action[1]
        else:
            self._final = True

    def read_symbol(self):
        return self._tape[self._tape.current_index]

    def write_symbol(self, symbol):
        self._tape[self._tape.current_index] = symbol

    def erase_symbol(self):
        self.write_symbol(self.blank)

    def move_head_right(self):
        self._tape.move_right()

    def move_head_left(self):
        self._tape.move_left()

    def print_tape(self, prompt=''):
        print '{0}{1}'.format(prompt, self._tape)