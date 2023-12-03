from .FileReader import FileReader

MAXES = [12, 13, 14]

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)
        
        string_array = fr.get_string_array()

        return string_array