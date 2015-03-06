__author__ = 'slouchart'

from turing.program import ProgramBuilder
from turing.machines import TuringMachine, default_blank as blank

"""
   Computes the one's complement of a binary integer
"""

if __name__ == "__main__":
    prg = ProgramBuilder()

    prg.add_step('I', '0', 'write', '1', 'move_right', 'I')
    prg.add_step('I', '1', 'write', '0', 'move_right', 'I')
    prg.add_step('I', blank, 'null', None, 'null', 'F')

    machine = TuringMachine(symbols=['0', '1'],
                            states=['I', 'F'],
                            initial='I',
                            finals=['F'],
                            transitions=prg.get_transition_table(), initial_input="001100")
    machine.print_tape('INPUT=')
    machine.run()
    machine.print_tape('OUTPUT=')
