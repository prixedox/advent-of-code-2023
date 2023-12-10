import numpy as np

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

    def traverse(self):
        cur_pos = self.get_start_position()
        last_pos = cur_pos
        cur_pos = self.find_initial_way(cur_pos)
        i = 1
        while self.grid[cur_pos[0], cur_pos[1]] != "S":
            last_pos, cur_pos = self.move(last_pos, cur_pos)
            i+=1
        print(i)
        return i / 2

    def get_start_position(self):
        start = np.where(self.grid == "S")
        return np.array([start[0][0], start[1][0]])
    
    def find_initial_way(self, cur_pos):
        
        idx = cur_pos + UP
        if self.grid[idx[0], idx[1]] in ["|", "F", "7"]:
            print(self.grid[idx[0], idx[1]])
            return idx

        idx = cur_pos + RIGHT
        if self.grid[idx[0], idx[1]] in ["-", "J", "7"]:
            print(self.grid[idx[0], idx[1]])
            return idx

        idx = cur_pos + DOWN
        if self.grid[idx[0], idx[1]] in ["|", "L", "J"]:
            print(self.grid[idx[0], idx[1]])
            return idx
        
        idx = cur_pos + LEFT
        if self.grid[idx[0], idx[1]] in ["-", "F", "L"]:
            print(self.grid[idx[0], idx[1]])
            return idx
    
    def move(self, last_pos, cur_pos):
        last_dir = last_pos - cur_pos
        char = self.grid[cur_pos[0], cur_pos[1]]
        next_dir = self.select_other_index(char, last_dir)
        last_pos = cur_pos
        cur_pos = cur_pos + next_dir
        print(last_pos, cur_pos)
        return last_pos, cur_pos
    

    def select_other_index(self, char, dir_):
        arr = RULES[char]
        if (arr[0] == dir_).all():
            return arr[1]
        else:
            return arr[0]
