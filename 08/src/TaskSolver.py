from .FileReader import FileReader
from .StringParser import StringParser
from .Traverser import Traverser
from .LowestCommonMultiple import LowestCommonMultiple

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        path, map_ = sp.parse_array()
        t = Traverser()
        if not is_part_two:
            steps = t.traverse(path, map_)
        else:
            steps = t.traverse_multiple(path, map_)
            lcm = LowestCommonMultiple()
            steps = lcm.calculate_lcm(steps)

        return steps