import numpy as np

class GalaxyDistance:

    def __init__(self, grid, empty_indexes):
        self.grid: np.ndarray = grid
        self.empty_indexes = empty_indexes

    def get_galaxy_distance(self):
        galaxies = self.get_galaxy_indexes()
        sum_ = 0

        for i in range(len(galaxies[0])):
            coords_i = (galaxies[0][i], galaxies[1][i])
            for j in range(i, len(galaxies[0])):
                if i == j:
                    continue
                coords_j = (galaxies[0][j], galaxies[1][j])

                sum_ += self.expand_by_val(coords_i, coords_j, 1000000)

                sum_ += abs(coords_i[0] - coords_j[0])
                sum_ += abs(coords_i[1] - coords_j[1])
        
        return sum_

    def get_galaxy_indexes(self):
        res = np.where(self.grid == "#")
        return res

    def expand_by_val(self, coords_i, coords_j, val):
        sum_ = 0
        start = coords_i[0]
        end = coords_j[0]
        if coords_i[0] > coords_j[0]:
            start = coords_j[0]
            end = coords_i[0]

        for k in range(start, end):
            if k in self.empty_indexes[0]:
                sum_ += val - 1

        start = coords_i[1]
        end = coords_j[1]
        if coords_i[1] > coords_j[1]:
            start = coords_j[1]
            end = coords_i[1]
        
        for k in range(start, end):
            if k in self.empty_indexes[1]:
                sum_ += val - 1
        
        return sum_