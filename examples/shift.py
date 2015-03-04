__author__ = 'slouchart'


"""
   shift the input to the right by one position
"""

from turing.program import ProgramBuilder
from turing.machines import TuringMachine


if __name__ == "__main__":
    prg = ProgramBuilder()
    blank = TuringMachine.blank

    prg.add_step('I', '0', 'write', '0', 'null', 'e1')
    prg.add_step('I', '1', 'write', '1', 'null', 'e2')

    prg.add_step('e1', '0', 'erase', None, 'move_right', 'e3')
    prg.add_step('e2', '1', 'erase', None, 'move_right', 'e4')

    prg.add_step('e3', blank, 'write', '0', 'move_left', 'e5')
    prg.add_step('e4', blank, 'write', '1', 'move_left', 'e5')

    prg.add_step('e5', blank, 'null', None, 'move_left', 'e5')

    prg.add_step('e5', '0', 'write', '0', 'null', 'e1')
    prg.add_step('e5', '1', 'write', '1', 'null', 'e2')

    prg.add_step('e5', 'S', 'null', None, 'null', 'F')

    machine = TuringMachine(input="",
                            symbols=['0', '1', 'S'],
                            states=['I', 'e1', 'e2', 'e3', 'e4', 'e5', 'F'],
                            initial='I',
                            finals=['F'],
                            transitions=prg.get_transition_table())

    machine.write_symbol('S')
    machine.move_head_right()
    machine.write_symbol('1')
    machine.move_head_right()
    machine.write_symbol('0')
    machine.move_head_right()
    machine.write_symbol('1')

    machine.print_tape('INPUT=')
    machine.run()

    machine.print_tape('OUTPUT=')




