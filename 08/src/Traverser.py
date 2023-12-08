class Traverser:

    def __init__(self):
        pass

    def traverse(self, path, map_):
        cur_elm = "AAA"
        print(cur_elm)
        steps = 0
        i = 0
        while True:
            if path[i] == "R":
                cur_elm = map_[cur_elm][1]
            elif path[i] == "L":
                cur_elm = map_[cur_elm][0]

            i += 1
            if i >= len(path):
                i = 0

            steps += 1
            #print(cur_elm)
            if cur_elm == "ZZZ":
                return steps
                