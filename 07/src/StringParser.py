class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
        self.cards_list = []
        self.score_dict = {}
    
    def parse_cards_and_score(self):
        for string in self.string_array:
            cards, score = string.split(" ")
            self.cards_list.append(cards)
            self.score_dict[cards] = score
        
        return self.cards_list, self.score_dict