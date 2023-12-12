class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        springs = []
        numbers = []
        for string_line in self.string_array:
            springs.append(string_line.split(" ")[0])
            
            numbers_group = string_line.split(" ")[1]

            converted_number_group = []
            for number in numbers_group.split(","):
                converted_number_group.append(int(number))
                
            numbers.append(converted_number_group)
        
        return springs, numbers