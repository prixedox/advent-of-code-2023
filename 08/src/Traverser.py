class Traverser:

    def __init__(self):
        pass

    def traverse(self, path, map_):
        cur_elm = "AAA"
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
    
    def traverse_multiple(self, path, map_):
        cur_elms = [item for item in list(map_.keys()) if item[2] == "A"]
        
        steps_list = []
        for j, cur_elm in enumerate(cur_elms):
            steps = 0
            i = 0
            while True:
                print(cur_elms, steps)
                
                
                if path[i] == "R":
                    cur_elms[j] = map_[cur_elms[j]][1]
                elif path[i] == "L":
                    cur_elms[j] = map_[cur_elms[j]][0]

                i += 1
                if i >= len(path):
                    i = 0

                steps += 1
                
                if cur_elms[j][2] == "Z":
                    steps_list.append(steps)
                    break
                
                    
        return steps_list