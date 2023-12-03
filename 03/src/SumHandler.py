class SumHandler:
    
    def __init__(self):
        pass
    
    def sum_list_strings(self, lst_strings):
        sum_ = 0
        new_list = []
        #print(lst_strings)
        for number_position in lst_strings:
            new_list.append(int(number_position))
            sum_ += int(number_position)
        
        return sum_