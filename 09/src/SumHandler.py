from .Predictor import Predictor


class SumHandler:
    
    def __init__(self):
        pass
    
    def make_sum(self, lines):
        result_list = []
        for line in lines:
            p = Predictor(line)
            result_list.append(p.get_predicted_values())
            
        return result_list