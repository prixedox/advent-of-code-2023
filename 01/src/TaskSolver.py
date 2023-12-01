from .FileReader import FileReader
from .StringParser import StringParser
from .NumberHandler import NumberHandler

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)
        string_array = fr.get_string_array()
        sp = StringParser()
        numbers_string_array = sp.get_first_and_last_numbers(string_array, is_part_two)
        nh = NumberHandler()
        result = nh.make_sum(numbers_string_array)

        return result