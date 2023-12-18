import numpy as np
from scipy import ndimage



class Traverser:

    def __init__(self, lines):
        self.lines = lines

    def traverse(self):
        self.set_grid_and_start()
        cur_pos = [self.start[0], self.start[1]]
        self.grid[cur_pos[0], cur_pos[1]] = 1

        for line in self.lines:
            for i in range(line[1]):
                if line[0] == "R":
                    cur_pos[1] += 1
                elif line[0] == "L":
                    cur_pos[1] -= 1
                elif line[0] == "U":
                    cur_pos[0] -= 1
                elif line[0] == "D":
                    cur_pos[0] += 1
                
                self.grid[cur_pos[0], cur_pos[1]] = 1
        
        self.grid = ndimage.binary_fill_holes(self.grid).astype(int)
        return np.sum(self.grid)
        #print(self.grid)
        #np.savetxt("test.txt", self.grid, fmt="%d")

    
    def set_grid_and_start(self):
        min_r, max_r, min_c, max_c = self.get_grid_dimensions()
        rows = max_r - min_r + 1
        cols = max_c - min_c + 1
        self.grid = np.zeros((rows, cols), dtype=int)
        self.start = (abs(min_r), abs(min_c))
        print(self.grid, self.start)
        print(self.grid.shape)

    def get_grid_dimensions(self):
        r = 0
        c = 0
        min_r = r
        max_r = r
        min_c = c
        max_c = c

        for line in self.lines:
            if line[0] == "R":
                c += line[1]
                if c > max_c:
                    max_c = c
            elif line[0] == "L":
                c -= line[1]
                if c < min_c:
                    min_c = c
            elif line[0] == "U":
                r -= line[1]
                if r < min_r:
                    min_r = r
            elif line[0] == "D":
                r += line[1]
                if r > max_r:
                    max_r = r
        
        return (min_r, max_r, min_c, max_c)