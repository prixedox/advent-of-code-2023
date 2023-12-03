class StringParser:

    def __init__(self, string_array):
        self.numbers_positions = []
        self.string_array = string_array
        self.board_size = self.get_board_size()
    
    def get_board_size(self):
        rows = len(self.string_array)
        cols = len(self.string_array[0])
        return [rows, cols]

    def get_numbers_with_positions(self):
        for i, string in enumerate(self.string_array):
            number_position = []
            number = ""
            number_started = False
            for j, char in enumerate(string):
                if char.isdigit() and not number_started:
                    number = char
                    number_position = [i, j]
                    number_started = True
                elif char.isdigit() and number_started:
                    number += char
                elif number_started:
                    self.numbers_positions.append([number, number_position])
                    number_started = False
                    number = ""
                    
        return self.numbers_positions
    
    def has_adjaced_symbol(self):
        pass
    
    def get_surroundings(self):
        i_start = 0
        i_end = 0
        j_start = 0
        j_end = 0

    
