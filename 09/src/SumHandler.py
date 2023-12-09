from .Predictor import Predictor


class SumHandler:
    
    def __init__(self):
        pass
    
    def make_sum(self, lines, is_part_two):
        result_list = []
        for line in lines:
            if is_part_two:
                line = line[::-1]
            p = Predictor(line)
            result_list.append(p.get_predicted_values())
            
        return result_list