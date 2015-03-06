__author__ = 'slouchart'


class Tape(object):
    def __init__(self, blank, input=""):
        self._tape = {}
        for i in range(len(input)):
            self._tape[i] = input[i]
        self._current_index = 0
        self.blank = blank

    @property
    def current_index(self):
        return self._current_index

    def move_left(self):
        self._current_index -= 1

    def move_right(self):
        self._current_index += 1

    def __getitem__(self, item):
        try:
            return self._tape[item]
        except KeyError:
            return self.blank

    def __setitem__(self, key, value):
        self._tape[key] = value

    def __str__(self):
        output = ''
        start = min(self._tape.iterkeys())
        end = max(self._tape.iterkeys())
        for i in range(start, end + 1):
            output += self._tape[i]
        return output

if __name__ == "__main__":
    """
    unit testing
    """
    tape = Tape("010101")
    print tape
    tape[0] = tape[1]
    print tape
