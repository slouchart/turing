__author__ = 'slouchart'

"""
    Turing's own basic example. Machine that computes the serie: 0 b 1 b 0 b 1 etc
"""

from turing.program import ProgramBuilder
from turing.machines import TuringMachine

if __name__ == "__main__":
    prg = ProgramBuilder()
    blank = TuringMachine.blank

    prg.add_step('e0', blank, 'write', '0', 'move_right', 'e1')
    prg.add_step('e1', blank, 'write', blank, 'move_right', 'e2')
    prg.add_step('e2', blank, 'write', '1', 'move_right', 'e3')
    prg.add_step('e3', blank, 'write', blank, 'move_right', 'e0')

    prg.add_step('e0', 'S', 'null', None, 'null', 'F')
    prg.add_step('e1', 'S', 'null', None, 'null', 'F')
    prg.add_step('e2', 'S', 'null', None, 'null', 'F')
    prg.add_step('e3', 'S', 'null', None, 'null', 'F')

    machine = TuringMachine(input="",
                            symbols=['0', '1', 'S'],
                            states=['e0', 'e1', 'e2', 'e3', 'e4', 'F'],
                            initial='e0',
                            finals=['F'],
                            transitions=prg.get_transition_table())

    machine.write_symbol('S')  # a stop word (i.e. minimization)
    machine.move_head_left()
    machine.move_head_left()
    machine.move_head_left()
    machine.move_head_left()
    machine.move_head_left()
    machine.move_head_left()
    machine.move_head_left()
    machine.move_head_left()

    machine.print_tape('INPUT=')
    machine.run()
    machine.print_tape('OUTPUT=')