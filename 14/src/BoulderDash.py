class BoulderDash:

    def __init__(self, grid):
        self.grid = grid
        self.cycles = []
    
    def do_cycle(self):
        for i in range(300):
            self.move_north()
            self.move_west()
            self.move_south()
            self.move_east()
            self.cycles.append(self.sum_boulders())

        
        period = self.get_period()
        start_idx = len(self.cycles)-(period+1)
        mod = (1000000000-start_idx-1) % period
        res = self.cycles[start_idx + mod]

        return res
        

    
    def get_period(self):
        j = 1
        found = False
        period = 0
        while not found:
            indices = [i for i, x in enumerate(self.cycles) if x == self.cycles[-j]]
            found = False
            for i in range(len(indices) - 2):
                if indices[i+1] - indices[i] == indices[i+2] - indices[i+1]:
                    found = True
                    period = indices[i+1] - indices[i]
                else:
                    found = False
                    break
            j += 1

        return period

    def move_north(self):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j] == "O":
                    k = i - 1
                    while k >= 0:
                        if self.grid[k, j] == ".":
                            self.grid[k+1, j] = "."
                            self.grid[k, j] = "O"
                        else:
                            break
                        k -= 1

    def move_west(self):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j] == "O":
                    k = j - 1
                    while k >= 0:
                        if self.grid[i, k] == ".":
                            self.grid[i, k+1] = "."
                            self.grid[i, k] = "O"
                        else:
                            break
                        k -= 1
    
    def move_south(self):
        for i in range(self.grid.shape[0] - 1, -1, -1):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j] == "O":
                    k = i + 1
                    while k < self.grid.shape[0]:
                        if self.grid[k, j] == ".":
                            self.grid[k-1, j] = "."
                            self.grid[k, j] = "O"
                        else:
                            break
                        k += 1

    def move_east(self):
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1] -1, -1, -1):
                if self.grid[i,j] == "O":
                    k = j + 1
                    while k < self.grid.shape[1]:
                        if self.grid[i, k] == ".":
                            self.grid[i, k-1] = "."
                            self.grid[i, k] = "O"
                        else:
                            break
                        k += 1
    
    def sum_boulders(self):
        sum_ = 0
        size = self.grid.shape[0]
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i,j] == 'O':
                    sum_ += size - i
        
        return sum_
