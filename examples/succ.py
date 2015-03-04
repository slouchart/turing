__author__ = 'slouchart'


from turing.program import ProgramBuilder
from turing.machines import TuringMachine

"""
   Computes the successor of a binary integer
"""

if __name__ == "__main__":
    prg = ProgramBuilder()
    blank = TuringMachine.blank

    prg.add_step('I', blank, 'write', blank, 'move_left', 'I')
    prg.add_step('I', '0', 'write', '1', 'move_left', 'A')
    prg.add_step('I', '1', 'write', '0', 'move_left', 'B')

    prg.add_step('A', '0', 'write', '0', 'move_left', 'A')
    prg.add_step('A', '1', 'write', '1', 'move_left', 'A')
    prg.add_step('A', blank, 'null', None, 'null', 'F')

    prg.add_step('B', '0', 'write', '1', 'move_left', 'A')
    prg.add_step('B', '1', 'write', '0', 'move_left', 'B')
    prg.add_step('B', blank, 'write', '1', 'null', 'F')

    machine = TuringMachine(input="",
                            symbols=['0', '1'],
                            states=['I', 'A', 'B', 'F'],
                            initial='I',
                            finals=['F'],
                            transitions=prg.get_transition_table())

    machine.write_symbol('1')
    machine.move_head_right()
    machine.write_symbol('1')
    machine.move_head_right()
    machine.write_symbol('1')
    machine.move_head_right()
    machine.write_symbol('1')
    machine.move_head_right()

    machine.print_tape('INPUT=')
    machine.run()

    machine.print_tape('OUTPUT=')
