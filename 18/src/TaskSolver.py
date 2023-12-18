from .FileReader import FileReader
from .StringParser import StringParser
from .Traverser import Traverser
from .Shoelace import Shoelace

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        lines = sp.parse_array()

        # t = Traverser(lines)
        # sum_ = t.traverse()
        sl = Shoelace(lines)
        sum_ = sl.shoelace_area()

        return sum_