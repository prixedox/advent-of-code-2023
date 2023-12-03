from .FileReader import FileReader
from .StringParser import StringParser
from .SumHandler import SumHandler

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)
        string_array = fr.get_string_array()
        
        #sum_ = self.solve_task_one(string_array)
        sum_ = self.solve_task_two(string_array)
        
        return sum_
    
    def solve_task_one(self, string_array):
        sp = StringParser(string_array)
        numbers_positions = sp.get_numbers_with_positions()
        
        sh = SumHandler()
        sum_ = sh.sum_list_strings(numbers_positions)

        return sum_
    
    def solve_task_two(self, string_array):
        sp = StringParser(string_array)
        numbers_to_mult = sp.get_numbers_adjaced_numbers()

        sh = SumHandler()
        sum_ = sh.mult_and_sum(numbers_to_mult)

        return sum_