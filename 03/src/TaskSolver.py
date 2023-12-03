from .FileReader import FileReader
from .StringParser import StringParser

MAXES = [12, 13, 14]

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)
        string_array = fr.get_string_array()
        
        sp = StringParser(string_array)
        numbers_positions = sp.get_numbers_with_positions()
        print(sp.board_size)
        

        return numbers_positions