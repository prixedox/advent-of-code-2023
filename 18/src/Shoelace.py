class Shoelace:

    def __init__(self, lines):
        self.lines = lines
        self.total = 0

    def get_dirs_from_hex(self):
        new_lines = []
        for line in self.lines:
            new_count = int(line[2][2:7], 16)
            new_dir = line[2][7]
            #print(new_count, new_dir)
            new_lines.append((new_dir, new_count))
        print(new_lines)
        return new_lines
    
    def shoelace_area(self):
        vertices = self.get_x_y_coords()

        A = 0
        for i in range(len(vertices)):
            if i == len(vertices)-1:
                A += vertices[i][0]*vertices[0][1] - vertices[i][1]*vertices[0][0]
            else:
                A += vertices[i][0]*vertices[i+1][1] - vertices[i][1]*vertices[i+1][0]
        return abs(A)//2 + self.total // 2 + 1

    def get_x_y_coords(self):
        new_lines = self.get_dirs_from_hex()
        start = self.get_starting_position()
        cur_pos = [start[0], start[1]]
        x_y_coords = []
        print(start)
        for line in new_lines:
            if line[0] == "0":
                cur_pos[1] += line[1]
            elif line[0] == "2":
                cur_pos[1] -= line[1]
            elif line[0] == "3":
                cur_pos[0] -= line[1]
            elif line[0] == "1":
                cur_pos[0] += line[1]

            self.total += line[1]
            x_y_coords.append((cur_pos[0], cur_pos[1]))
        
        print(x_y_coords)
        return x_y_coords


    def get_starting_position(self):
        new_lines = self.get_dirs_from_hex()
        r = 0
        c = 0
        min_r = r
        max_r = r
        min_c = c
        max_c = c

        for line in new_lines:
            if line[0] == "0":
                c += line[1]
                if c > max_c:
                    max_c = c
            elif line[0] == "2":
                c -= line[1]
                if c < min_c:
                    min_c = c
            elif line[0] == "3":
                r -= line[1]
                if r < min_r:
                    min_r = r
            elif line[0] == "1":
                r += line[1]
                if r > max_r:
                    max_r = r
        
        return (abs(min_r), abs(min_c))



    

