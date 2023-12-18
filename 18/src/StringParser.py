import numpy as np

class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        lines = []
        for i, string_line in enumerate(self.string_array):
            arr = string_line.split(" ")
            lines.append((arr[0], int(arr[1]), arr[2]))
        
        return lines