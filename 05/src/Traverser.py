class Traverser:
    
    def __init__(self):
        pass

    def get_seeds_location(self, info):
        locations = []
        for seed in info["seeds"]:
            if seed % 1000000 == 0:
                print(seed)
            map_ = [seed]
            for i in range(len(info["source"])):
                for j in range(len(info["source"][i])):
                    if map_[-1] >= info["source"][i][j] and map_[-1] <= info["source"][i][j] + info["count"][i][j]:
                        diff = info["dest"][i][j] - info["source"][i][j]
                        map_.append(map_[-1] + diff)
                        break
                if len(map_) - 1 == i:
                    map_.append(map_[-1])
            locations.append(map_[-1])

        return locations
    
    def traverse_backwards(self, info):
        found = False
        #number = 65700000
        number = 81900000
        while True:
            traverse_number = number
            for i in range(len(info["source"]) - 1, -1, -1):
                for j in range(len(info["source"][i])):
                    if traverse_number >= info["dest"][i][j] and traverse_number < info["dest"][i][j] + info["count"][i][j]:
                        diff = info["source"][i][j] - info["dest"][i][j]
                        #map_.append(map_[-1] + diff)
                        traverse_number = traverse_number + diff
                        break
                    #print(number, traverse_number)
                #print()
            for seed_group in info["seeds"]:
                if traverse_number >= seed_group[0] and traverse_number <= seed_group[1]:
                    print("found", number, traverse_number)
                    return number
            
            if number % 100000 == 0:
                print(number, traverse_number)
            number += 1
            