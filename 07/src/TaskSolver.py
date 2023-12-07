from .ScoreAdder import ScoreAdder
from .FileReader import FileReader
from .StringParser import StringParser

class TaskSolver:

    def __init__(self):
        pass
    
    def solve(self, filename, is_part_two):
        fr = FileReader(filename)

        string_array = fr.get_string_array()

        sp = StringParser(string_array)
        cards_list, score_dict = sp.parse_cards_and_score()

        sa = ScoreAdder()
        total_winnings = sa.get_total_winnings(cards_list, score_dict)
        

        return total_winnings