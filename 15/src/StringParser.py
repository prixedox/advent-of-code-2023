import numpy as np

class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        strings = self.string_array[0].split(",")
        
        return strings