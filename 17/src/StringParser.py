import numpy as np

class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        grid = np.zeros((len(self.string_array), len(self.string_array[0]))).astype(int)
        for i, string_line in enumerate(self.string_array):
            for j, char in enumerate(string_line):
                grid[i, j] = int(char)
        
        return grid