class GamesAdder:

    def __init__(self):
        pass

    def add_games(self, possible_games_list):
        sum_ = 0
        for i, possible_game in enumerate(possible_games_list):
            if possible_game:
                sum_ += i+1
        return sum_
    
    def multiply_amounts(self, max_amounts):
        total_sum = 0
        for max_amount in max_amounts:
            total_sum += max_amount[0] * max_amount[1] * max_amount[2]
        
        return total_sum