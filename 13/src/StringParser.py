import numpy as np

class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        grids = []
        grid = []
        for i, string_line in enumerate(self.string_array):
            line = []
            if string_line == "":
                grids.append(grid)
                grid = []

            elif string_line != "\n":
                for j, char in enumerate(string_line):
                    line.append(char)
                grid.append(line)

        grids.append(grid)
        
            
        
        return grids