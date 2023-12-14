from .FileReader import FileReader
from .StringParser import StringParser
from .Possibilities import Possibilities
from .Filter import Filter

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        springs, numbers = sp.parse_array()

        p = Possibilities()
        
        if not is_part_two:
            pos_springs = p.extend(springs)

            f = Filter()
            sum_ = f.filter(pos_springs, numbers)
        else:
            sum_ = p.get_number_of_possibilities(springs, numbers)
        
        return sum_