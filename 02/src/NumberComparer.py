class NumberComparer:

    def __init__(self, maxes):
        self.maxes = maxes

    def compare(self, games):
        is_possible_list = []
        for game in games:
            is_possible_game = True
            if self.maxes[0] < game[0]:
                is_possible_game = False
            elif self.maxes[1] < game[1]:
                is_possible_game = False
            elif self.maxes[2] < game[2]:
                is_possible_game = False

            is_possible_list.append(is_possible_game)

        return is_possible_list
            
