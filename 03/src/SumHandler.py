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
    
    def mult_and_sum(self, lst_strings):
        sum_ = 0
        print(lst_strings)
        for number_group in lst_strings:
            sum_ += int(number_group[0]) * int(number_group[1])
        
        return sum_