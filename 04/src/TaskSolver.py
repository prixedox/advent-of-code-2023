from .FileReader import FileReader
from .StringParser import StringParser
from .CompareHandler import CompareHandler

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()
        sp = StringParser(string_array)
        games_array = sp.get_game_array()

        ch = CompareHandler()
        games_points = ch.get_points_per_game(games_array)

        return games_points