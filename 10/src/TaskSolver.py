from .Traverser import Traverser
from .FileReader import FileReader
from .StringParser import StringParser

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        grid = sp.parse_array()
        t = Traverser(grid)
        steps = t.traverse()
        
        return steps