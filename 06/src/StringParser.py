class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
        self.races = {}
    
    def parse_time_and_distances(self, is_part_two):
        self.races["times"] = self.string_array[0].split(":")[1]
        self.races["distances"] = self.string_array[1].split(":")[1]

        if is_part_two:
            self.races["times"] = self.connect_numbers(self.races["times"])
            self.races["distances"] = self.connect_numbers(self.races["distances"])
        else:
            self.races["times"] = self.process_array(self.races["times"])
            self.races["distances"] = self.process_array(self.races["distances"])

        return self.races
    
    def process_array(self, array):
        array = array.split(" ")
        array = self.remove_empty_elements(array)
        array = self.parse_to_int(array)
        return array
    
    def connect_numbers(self, array):
        array = array.replace(" ", "")
        array = [int(array)]
        return array

    def remove_empty_elements(self, array):
        new_array = []
        for item in array:
            if item != "":
                new_array.append(item)
        return new_array
    
    def parse_to_int(self, array):
        new_array = []
        for item in array:
            new_array.append(int(item))
        return new_array