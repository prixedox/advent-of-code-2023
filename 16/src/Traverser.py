import numpy as np

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIR_SLASH = {UP: RIGHT, RIGHT: UP, DOWN: LEFT, LEFT: DOWN}
DIR_BACKSLASH = {UP: LEFT, LEFT: UP, DOWN: RIGHT, RIGHT: DOWN}

class Traverser:

    def __init__(self, grid):
        self.grid = grid
        self.visited = np.zeros((self.grid.shape))
        self.unique = np.zeros((self.grid.shape))
    
    def traverse_multiple(self):
        sums = []
        length = self.grid.shape[0]
        for i in range(0, length):
            sums.append(self.traverse([0, i], DOWN))
            print(i, "down")
            sums.append(self.traverse([length, i], UP))
            print(i, "up")
            sums.append(self.traverse([i, length], LEFT))
            print(i, "left")
            sums.append(self.traverse([i, 0], RIGHT))
            print(i, "right")
            
            print(sums[-4:])
            print("cur max:", max(sums))
        return sums

    def traverse(self, cur_pos, cur_dir):
        self.visited = np.zeros((self.grid.shape))
        self.unique = np.zeros((self.grid.shape))

        cur_positions = [cur_pos]
        cur_directions = [cur_dir]
        since_last_change = 0
        last_sum = 0
        while cur_positions and since_last_change < 10:
            
            if np.sum(self.visited) == last_sum:
                since_last_change += 1
            else:
                since_last_change = 0
                last_sum = np.sum(self.visited)
            #print(last_sum, since_last_change)
            i = 0
            
            while i < len(cur_positions):                
                
                if cur_positions[i][0] < 0 or cur_positions[i][1] < 0 or \
                cur_positions[i][0] >= self.grid.shape[0] or cur_positions[i][1] >= self.grid.shape[1]:
                    del cur_positions[i]
                    del cur_directions[i]
                    continue
                

                

                self.visited[cur_positions[i][0], cur_positions[i][1]] = 1

                char_pos = self.grid[cur_positions[i][0], cur_positions[i][1]]
                #print(char_pos, cur_positions, cur_directions)
                if char_pos == ".":
                    self.unique[cur_positions[i][0], cur_positions[i][1]] = 1
                elif char_pos == "\\":
                    cur_directions[i] = self.get_mirror_dir(cur_directions[i], char_pos)
                    self.unique[cur_positions[i][0], cur_positions[i][1]] = 1
                elif char_pos == "/":
                    cur_directions[i] = self.get_mirror_dir(cur_directions[i], char_pos)
                    self.unique[cur_positions[i][0], cur_positions[i][1]] = 1
                elif char_pos == "|":
                    if cur_directions[i] == LEFT or cur_directions[i] == RIGHT:
                        cur_directions[i] = UP
                        cur_directions.append(DOWN)
                        cur_positions.append(cur_positions[i].copy())
                        self.unique[cur_positions[i][0], cur_positions[i][1]] = 1
                elif char_pos == "-":
                    if cur_directions[i] == UP or cur_directions[i] == DOWN:
                        cur_directions[i] = LEFT
                        cur_directions.append(RIGHT)
                        cur_positions.append(cur_positions[i].copy())
                        self.unique[cur_positions[i][0], cur_positions[i][1]] = 1
                
                

                cur_positions[i][0] += cur_directions[i][0]
                cur_positions[i][1] += cur_directions[i][1]

                if cur_positions[i][0] < 0 or cur_positions[i][1] < 0 or \
                cur_positions[i][0] >= self.grid.shape[0] or cur_positions[i][1] >= self.grid.shape[1]:
                    del cur_positions[i]
                    del cur_directions[i]
                    continue
                
                # if self.unique[cur_positions[i][0], cur_positions[i][1]] == 1:
                #     del cur_positions[i]
                #     del cur_directions[i]
                #     continue
                

                i += 1
        
        return np.sum(self.visited)

    def get_mirror_dir(self, cur_dir, mirror):
        if mirror == "\\":
            return DIR_BACKSLASH[cur_dir]
        else:
            return DIR_SLASH[cur_dir]