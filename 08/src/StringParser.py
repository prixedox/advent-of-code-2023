class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
        self.path = ""
        self.map = {}
    
    def parse_array(self):
        self.path = self.string_array[0]

        for i, string in enumerate(self.string_array):
            if i < 2:
                continue
            
            trail = string.split(" = ")
            left_right = trail[1].replace("(", "").replace(")", "").split(", ")
            self.map[trail[0]] = (left_right[0], left_right[1])

        return self.path, self.map
            