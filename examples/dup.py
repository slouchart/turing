__author__ = 'slouchart'

"""
 Duplicate the content of the tape
  INPUT = 101000110S
 OUTPUT = 101000110S101000110S
"""

from turing.program import ProgramBuilder
from turing.machines import TuringMachine, default_blank as blank


if __name__ == "__main__":

    prg = ProgramBuilder()

    prg.add_step('I', '0', 'null', None, 'move_right', 'I')
    prg.add_step('I', '1', 'null', None, 'move_right', 'I')

    machine = TuringMachine(initial_input="S101000110",
                            symbols=['0', '1', 'S'],
                            states=['I', 'e1', 'e2', 'e3', 'e4', 'e5', 'F'],
                            initial='I',
                            finals=['F'],
                            transitions=prg.get_transition_table())



    machine.print_tape('INPUT=')
    machine.run()
    machine.print_tape('OUTPUT=')