class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
        self.info = {}
    
    def get_info(self):
        self.parse_seeds()
        self.parse_maps()
        return self.info
    
    def parse_seeds(self):
        seeds = []
        numbers = self.string_array[0].split(": ")[1]
        for number in numbers.split(" "):
            seeds.append(int(number))
        self.info["seeds"] = seeds
    
    def parse_maps(self):
        source_list = []
        dest_list = []
        count_list = []
        self.info["source"] = []
        self.info["dest"] = []
        self.info["count"] = []
        for line in self.string_array[3:]:
            if line == "":
                continue
            elif "map" in line:
                self.info["source"].append(source_list)
                self.info["dest"].append(dest_list)
                self.info["count"].append(count_list)
                source_list = []
                dest_list = []
                count_list = []
            else:
                dest, source, count = line.split(" ")
                dest_list.append(int(dest))
                source_list.append(int(source))
                count_list.append(int(count))

        self.info["source"].append(source_list)
        self.info["dest"].append(dest_list)
        self.info["count"].append(count_list)