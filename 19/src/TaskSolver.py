from .FileReader import FileReader
from .StringParser import StringParser
from .Filter import Filter
from .Intervals import Intervals

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        rules, parts = sp.parse_array()

        # f = Filter(rules, parts)
        # res = f.filter_parts()
        i = Intervals(rules)
        i.traverse_single()

        return None