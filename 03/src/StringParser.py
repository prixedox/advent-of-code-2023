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

    def get_numbers_adjaced_numbers(self):
        star_positions = self.get_star_positions()
        digit_positions = self.get_numbers_adjaced_star(star_positions)
        number_positions = self.get_star_groups(digit_positions)

        numbers_to_mult = []
        for number_group in number_positions:
            if len(number_group) < 2:
                continue
            number_group_list = []
            for number_position in number_group:
                i = number_position[1]
                number = ""
                while i < len(self.string_array[0]) and self.string_array[number_position[0]][i].isdigit():
                    number += self.string_array[number_position[0]][i]
                    i += 1
                number_group_list.append(number)
            numbers_to_mult.append(number_group_list)
        
                
                
        return numbers_to_mult
    
    def get_star_positions(self):
        star_positions = []
        for i, string in enumerate(self.string_array):
            for j, char in enumerate(string):
                if char == "*":
                    star_positions.append([i, j])
        return star_positions
    
    def get_numbers_adjaced_star(self, star_positions):
        all_digit_positions = []
        for star_position in star_positions:
            digit_positions = []
            for i in [star_position[0] - 1, star_position[0], star_position[0] + 1]:
                for j in [star_position[1] - 1, star_position[1], star_position[1] + 1]:
                    if i < 0 or i > len(self.string_array) - 1 or j < 0 or j > len(self.string_array[0]) - 1:
                        continue
                    if self.string_array[i][j].isdigit():
                        digit_positions.append([i, j])
            all_digit_positions.append(digit_positions)
        
        return all_digit_positions
    
    def get_star_groups(self, digit_positions):
        star_groups = []
        first_pos = set()
        for digit_group in digit_positions:
            first_pos = set()
            for digit_position in digit_group:
                i = digit_position[1]
                while i >= 0 and self.string_array[digit_position[0]][i].isdigit():
                    i -= 1
                first_pos.add((digit_position[0], i+1))
            star_groups.append(first_pos)
        
        return star_groups
    