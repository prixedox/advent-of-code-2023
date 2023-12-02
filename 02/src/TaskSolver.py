from .FileReader import FileReader
from .StringParser import StringParser

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)
        string_array = fr.get_string_array()
        sp = StringParser()
        max_amount = sp.get_max_amount_in_game(string_array)

        return max_amount