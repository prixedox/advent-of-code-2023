CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
CARDS_2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

class CardComparer:

    def __init__(self, is_part_two):
        self.is_part_two = is_part_two

    def compare_cards(self, first, second):
        first_count = self.get_cards_count(first)
        second_count = self.get_cards_count(second)

        first_kind_score = self.get_kind_score(first_count)
        second_kind_score = self.get_kind_score(second_count)

        if first_kind_score > second_kind_score:
            return 1
        elif second_kind_score > first_kind_score:
            return -1
        else:
            return self.get_first_bigger_card(first, second)
    
    def get_first_bigger_card(self, first, second):
        for i in range(len(first)):
            if CARDS_2.index(first[i]) > CARDS_2.index(second[i]):
                return 1
            elif CARDS_2.index(second[i]) > CARDS_2.index(first[i]):
                return -1

    def get_cards_count(self, cards):
        count = {}
        for card in cards:
            if card not in count:
                count[card] = 1
            else:
                count[card] += 1
        
        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        return count
    
    def get_kind_score(self, count_dict):
        if self.is_5_kind(count_dict):
            return 6
        elif self.is_4_kind(count_dict):
            return 5
        elif self.is_full_house(count_dict):
            return 4
        elif self.is_3_kind(count_dict):
            return 3
        elif self.is_2_pair(count_dict):
            return 2
        elif self.is_1_pair(count_dict):
            return 1
        else:
            return 0

    def is_5_kind(self, count_dict):
        if not self.is_part_two or "J" not in count_dict:
            return len(count_dict) == 1
        else:
            return len(count_dict) <= 2

    def is_4_kind(self, count_dict):
        if not self.is_part_two or "J" not in count_dict:
            for key in count_dict:
                if count_dict[key] == 4:
                    return True
            return False
        else:
            #23JJJ, 233JJ, 2333J
            keys = list(count_dict.keys())
            for key in keys:
                if key != "J":
                    if count_dict[key] + count_dict["J"] == 4:
                        return True
            return False
    
    def is_full_house(self, count_dict):
        if not self.is_part_two or "J" not in count_dict:
            vals = list(count_dict.values())
            if len(vals) == 2 and vals[0] == 3 and vals[1] == 2:
                return True
            return False
        else:
            #2233J
            vals = list(count_dict.values())
            if len(vals) == 3 and vals[0] == 2 and vals[1] == 2:
                return True
            return False
    
    def is_3_kind(self, count_dict):
        if not self.is_part_two or "J" not in count_dict:
            vals = list(count_dict.values())
            if len(vals) == 3 and vals[0] == 3:
                return True
            return False
        else:
            #234JJ, 2344J
            vals = list(count_dict.values())
            if len(vals) == 4:
                return True
            return False

    def is_2_pair(self, count_dict):
        # nothing changes
        vals = list(count_dict.values())
        if len(vals) == 3 and vals[0] == 2 and vals[1] == 2:
            return True
        return False
    

    def is_1_pair(self, count_dict):
        if not self.is_part_two or "J" not in count_dict:
            vals = list(count_dict.values())
            if len(vals) == 4 and vals[0] == 2:
                return True
            return False
        else:
            #2345J
            vals = list(count_dict.values())
            return len(vals) == 5

cc = CardComparer(True)
result = cc.compare_cards("AAAA3", "AAAAA")
print(result)