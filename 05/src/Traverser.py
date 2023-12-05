class Traverser:
    
    def __init__(self):
        pass

    def get_seeds_location(self, info):
        locations = []
        for seed in info["seeds"]:
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