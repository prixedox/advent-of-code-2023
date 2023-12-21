from .FileReader import FileReader
from .StringParser import StringParser
from .StateChanger import StateChanger

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        lines = sp.parse_array()

        sc = StateChanger(lines)
        total = sc.cycle()

        return total