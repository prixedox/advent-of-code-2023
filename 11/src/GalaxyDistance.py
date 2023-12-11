import numpy as np

class GalaxyDistance:

    def __init__(self, grid):
        self.grid: np.ndarray = grid

    def get_galaxy_distance(self):
        galaxies = self.get_galaxy_indexes()
        count = 0
        sum_ = 0
        for i in range(len(galaxies[0])):
            coords_i = (galaxies[0][i], galaxies[1][i])
            for j in range(i, len(galaxies[0])):
                if i == j:
                    continue
                coords_j = (galaxies[0][j], galaxies[1][j])
                count += 1

                sum_ += abs(coords_i[0] - coords_j[0])
                sum_ += abs(coords_i[1] - coords_j[1])
        
        return sum_

    def get_galaxy_indexes(self):
        res = np.where(self.grid == "#")
        return res