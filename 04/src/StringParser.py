class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    

    def get_game_array(self):
        games_array = []
        win_numbers = []
        my_numbers = []
        for game in self.string_array:
            numbers_split = game.split(": ")[1]
            win_numbers, my_numbers = numbers_split.split(" | ")
            win_numbers = win_numbers.split(" ")
            my_numbers = my_numbers.split(" ")
        
            win_numbers = self.strings_to_int(win_numbers)
            my_numbers = self.strings_to_int(my_numbers)

            games_array.append([win_numbers, my_numbers])
        
        return games_array
        
    def strings_to_int(self, string_numbers):
        numbers = []
        for string_number in string_numbers:
            if string_number == "":
                continue
            numbers.append(int(string_number))

        return numbers