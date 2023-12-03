class StringParser:

    def __init__(self, string_array):
        self.numbers_positions = []
        self.string_array = string_array
        self.board_size = self.get_board_size()
        self.final_list = []
    
    def get_board_size(self):
        rows = len(self.string_array)
        cols = len(self.string_array[0])
        return [rows, cols]

    def get_numbers_with_positions(self):
        number_started = False
        for i, string in enumerate(self.string_array):
            if number_started:
                surroundings = self.get_surroundings(number, number_position)
                if self.has_adjaced_symbol(surroundings):
                    self.final_list.append(number)
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
                    surroundings = self.get_surroundings(number, number_position)
                    if self.has_adjaced_symbol(surroundings):
                        self.final_list.append(number)

                    self.numbers_positions.append([number, number_position])
                    number_started = False
                    number = ""
                    
        return self.final_list
    
    def has_adjaced_symbol(self, surroundings):
        for i in range(surroundings[0], surroundings[1] + 1):
            for j in range(surroundings[2], surroundings[3] + 1):
                if self.string_array[i][j] != "." and not self.string_array[i][j].isdigit():
                    return True
        return False
                
    
    def get_surroundings(self, number, number_position):
        i_start = number_position[0] - 1
        i_end = number_position[0] + 1
        j_start = number_position[1] - 1
        j_end = number_position[1] + len(number) - 1 + 1
        
        if i_start < 0:
            i_start = 0
        if i_end > self.board_size[0] - 1:
            i_end = self.board_size[0] - 1
        if j_start < 0:
            j_start = 0
        if j_end > self.board_size[1] - 1:
            j_end = self.board_size[1] - 1
        
        return [i_start, i_end, j_start, j_end]