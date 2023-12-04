class CompareHandler:
    
    def __init__(self):
        pass

    def get_points_per_game(self, games_array):
        games_points = []
        for game_group in games_array:
            points = 0
            win_numbers, my_numbers = game_group
            for win_number in win_numbers:
                for my_number in my_numbers:
                    if win_number == my_number:
                        points *= 2
                        if points == 0:
                            points = 1
            games_points.append(points)
        
        return games_points
            