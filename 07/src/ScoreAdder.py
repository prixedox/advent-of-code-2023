from .CardComparer import CardComparer

class ScoreAdder:

    def __init__(self):
        self.cc = CardComparer()

    def sort_cards(self, cards_list):
        for i in range(len(cards_list)):
            for j in range(len(cards_list)):
                if cards_list[i] == cards_list[j]:
                    continue
                if self.cc.compare_cards(cards_list[i], cards_list[j]) == -1:
                    cards_list[i], cards_list[j] = cards_list[j], cards_list[i]
        return cards_list

    def get_total_winnings(self, cards_list, score_dict):
        cards_list = self.sort_cards(cards_list)
        total_winnings = 0
        for i, cards in enumerate(cards_list):
            total_winnings += int(score_dict[cards]) * (i + 1)

        return total_winnings