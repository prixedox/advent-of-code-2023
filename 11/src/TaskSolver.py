from .GalaxyDistance import GalaxyDistance
from .FileReader import FileReader
from .StringParser import StringParser
from .Expander import Expander

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        grid = sp.parse_array()

        e = Expander(grid)
        empty_indexes = e.get_empty_lines()

        gd = GalaxyDistance(grid, empty_indexes)
        sum_ = gd.get_galaxy_distance()
        
        return sum_