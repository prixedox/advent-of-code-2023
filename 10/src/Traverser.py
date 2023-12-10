import numpy as np
import cv2

UP = np.array([-1, 0])
DOWN = np.array([1, 0])
LEFT = np.array([0, -1])
RIGHT = np.array([0, 1])

RULES = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "F": [RIGHT, DOWN],
    "7": [LEFT, DOWN],
}

class Traverser:

    def __init__(self, grid: np.ndarray):
        self.grid = grid
        self.route_grid = np.zeros(grid.shape, dtype=np.uint8)

    def traverse(self):
        cur_pos = self.get_start_position()
        self.route_grid[cur_pos[0], cur_pos[1]] = 1

        last_pos = cur_pos
        cur_pos = self.find_initial_way(cur_pos)
        self.route_grid[cur_pos[0], cur_pos[1]] = 1

        i = 1
        while self.grid[cur_pos[0], cur_pos[1]] != "S":
            last_pos, cur_pos = self.move(last_pos, cur_pos)
            i+=1

        self.get_number_of_in()

        print(self.route_grid)
        return i / 2

    def get_number_of_in(self):
        count = 0
        for i in range(self.route_grid.shape[0]):
            add_on = False
            for j in range(self.route_grid.shape[1]):
                if self.route_grid[i, j] == 2:
                    add_on = not add_on
                if self.route_grid[i, j] == 0 and add_on:
                    self.route_grid[i, j] = 3
                    count += 1
        
        print(count)

        

    def get_start_position(self):
        start = np.where(self.grid == "S")
        return np.array([start[0][0], start[1][0]])
    
    def find_initial_way(self, cur_pos):
        idx = cur_pos + UP
        if self.grid[idx[0], idx[1]] in ["|", "F", "7"]:
            return idx

        idx = cur_pos + RIGHT
        if self.grid[idx[0], idx[1]] in ["-", "J", "7"]:
            return idx

        idx = cur_pos + DOWN
        if self.grid[idx[0], idx[1]] in ["|", "L", "J"]:
            return idx
        
        idx = cur_pos + LEFT
        if self.grid[idx[0], idx[1]] in ["-", "F", "L"]:
            return idx

    def move(self, last_pos, cur_pos):
        last_dir = last_pos - cur_pos
        char = self.grid[cur_pos[0], cur_pos[1]]
        next_dir = self.select_other_index(char, last_dir)

        if char in ["F", "7", "|"]:
            self.route_grid[cur_pos[0], cur_pos[1]] = 2
        else:
            self.route_grid[cur_pos[0], cur_pos[1]] = 1
        print(last_pos, cur_pos)

        last_pos = cur_pos
        cur_pos = cur_pos + next_dir

        
        return last_pos, cur_pos
    

    def select_other_index(self, char, dir_):
        arr = RULES[char]
        if (arr[0] == dir_).all():
            return arr[1]
        else:
            return arr[0]
