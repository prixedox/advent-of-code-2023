from .FileReader import FileReader
from .StringParser import StringParser
from .Traverser import Traverser
from .SeedExtender import SeedExtender

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()
        sp = StringParser(string_array)
        info = sp.get_info()

        if is_part_two:
            se = SeedExtender()
            info["seeds"] = se.extend_seed(info["seeds"])

        t = Traverser()
        locations = t.get_seeds_location(info)
        print(locations)
        return min(locations)