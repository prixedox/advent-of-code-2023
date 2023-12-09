class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
        self.path = ""
        self.map = {}
    
    def parse_array(self):
        lines = []
        for string_line in self.string_array:
            string_numbers = string_line.split(" ")
            number_line = []
            for string_number in string_numbers:
                number_line.append(int(string_number))
            
            lines.append(number_line)
            
        return lines