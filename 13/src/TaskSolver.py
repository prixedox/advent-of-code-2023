from .FileReader import FileReader
from .StringParser import StringParser
from .MirrorFinder import MirrorFinder

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        grids = sp.parse_array()

        mf = MirrorFinder()
        total = mf.find_all(grids)
        
        return total