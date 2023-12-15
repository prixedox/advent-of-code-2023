from .FileReader import FileReader
from .StringParser import StringParser
from .AsciiSum import AsciiSum
from .BoxSorter import BoxSorter

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        strings = sp.parse_array()

        if is_part_two:
            bs = BoxSorter()
            sum_ = bs.process(strings)
        else:
            as_ = AsciiSum()
            sum_ = as_.get_sum_of_strings(strings)

        return sum_