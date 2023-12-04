class PointsHandler:
    
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

    def get_cards_per_game(self, games_array):
        games_cards = [1 for _ in range(len(games_array))]
        for i, game_group in enumerate(games_array):
            copies = 0
            win_numbers, my_numbers = game_group
            for win_number in win_numbers:
                for my_number in my_numbers:
                    if win_number == my_number:
                        copies += 1
            for j in range(copies):
                if i+j+1 > len(games_array) - 1:
                    continue
                games_cards[i+j+1] += games_cards[i]

        return games_cards
            