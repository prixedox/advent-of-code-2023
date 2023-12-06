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
            info["seeds"] = se.get_seeds_boundary(info["seeds"])
        print(info)
        t = Traverser()
        if not is_part_two:
            locations = t.get_seeds_location(info)
            return min(locations)
        else:
            minimum = t.traverse_backwards(info)
            return minimum