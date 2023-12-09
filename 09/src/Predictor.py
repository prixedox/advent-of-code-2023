import numpy as np

class Predictor:
    
    def __init__(self, vals):
        self.init_matrix(vals)
    
    def init_matrix(self, vals):
        self.triangle_matrix = np.zeros((len(vals), len(vals) + 1)).astype(int)
        for i in range(len(vals)):
            self.triangle_matrix[0][i] = vals[i]
    
    def get_predicted_values(self):
        self.construct_triangle_array()
        self.predict_value()
        return self.triangle_matrix[0, -1]
    
    def construct_triangle_array(self):
        stop_idx = self.triangle_matrix.shape[0] - 1
        for i in range(1, self.triangle_matrix.shape[0]):
            for j in range(stop_idx):
                self.triangle_matrix[i, j] = self.triangle_matrix[i-1, j+1] - self.triangle_matrix[i-1, j] 
            if sum(self.triangle_matrix[i]) == 0:
                break
            stop_idx -= 1
    
    def predict_value(self):
        total_inc = 0
        for i in range(self.triangle_matrix.shape[0] - 1, -1, -1):
            if sum(self.triangle_matrix[i]) == 0:
                continue
            
            predict_idx = self.triangle_matrix.shape[0] - i
            self.triangle_matrix[i, predict_idx] = self.triangle_matrix[i, predict_idx - 1] + total_inc + \
                                                    (self.triangle_matrix[i, predict_idx - 1] - self.triangle_matrix[i, predict_idx - 2])
            total_inc += (self.triangle_matrix[i, predict_idx - 1] - self.triangle_matrix[i, predict_idx - 2])
                                                    

#vals = [0,3,6,9,12,15]
#vals = [1,3,6,10,15,21]
# vals = [10, 13, 16, 21, 30, 45]
# p = Predictor(vals)
# print(p.get_predicted_values())