import numpy as np

class StringParser:

    def __init__(self, string_array):
        self.string_array = string_array
    
    def parse_array(self):
        rules_dic = {}
        for i, string_line in enumerate(self.string_array):
            if string_line == "":
                break
            arr = string_line[:-1].split("{")
            key = arr[0]
            rules = arr[1].split(",")
            rules_to_add = []
            for rule in rules:
                splitted_rule = rule.split(":")
                if len(splitted_rule) == 1:
                    rules_to_add.append(("", splitted_rule[0]))
                else:
                    rules_to_add.append((splitted_rule[0], splitted_rule[1]))
            rules_dic[key] = rules_to_add
        
        parts_list = []
        for string_line in self.string_array[i+1:]:
            to_eval = string_line.replace("=", ":").replace("x", "'x'") \
                        .replace("m", "'m'").replace("s", "'s'").replace("a", "'a'")
            parts_list.append(eval(to_eval))
        
        return rules_dic, parts_list