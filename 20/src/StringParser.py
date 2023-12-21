import numpy as np

class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        lines = []
        for line in self.string_array:
            if line[0] == "b":
                pass
            elif line[0] == "%":
                pass
            elif line[0] == "&":
                pass

            var, target = line.split(" -> ")
            var = var[1:]
            target = target.split(", ")

            lines.append((line[0], var, target))
        
        return lines
