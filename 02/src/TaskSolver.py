from .FileReader import FileReader
from .StringParser import StringParser
from .NumberComparer import NumberComparer
from .GamesAdder import GamesAdder

MAXES = [12, 13, 14]

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)
        sp = StringParser()
        nc = NumberComparer(MAXES)
        ga = GamesAdder()

        string_array = fr.get_string_array()
        max_amount = sp.get_max_amount_in_game(string_array)

        if is_part_two:
            sum_ = ga.multiply_amounts(max_amount)
        else:
            possible_games_list = nc.compare(max_amount)
            sum_ = ga.add_games(possible_games_list)
        return sum_