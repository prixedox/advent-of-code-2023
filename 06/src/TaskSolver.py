from .FileReader import FileReader
from .StringParser import StringParser
from .RaceMaker import RaceMaker
from .ResultAdjuster import ResultAdjuster

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()
        sp = StringParser(string_array)
        races = sp.parse_time_and_distances(is_part_two)
        rm = RaceMaker()
        beated_array = rm.make_races(races)
        
        if is_part_two:
            return beated_array
        
        ra = ResultAdjuster()
        mult = ra.multiply_array(beated_array)

        return mult