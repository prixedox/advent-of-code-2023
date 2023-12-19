class Intervals:

    def __init__(self, rules):
        self.rules = rules
    
    def traverse_single(self):
        x = [(1, 4000)]
        m = [(1, 4000)]
        a = [(1, 4000)]
        s = [(1, 4000)]
        cur_abb = "in"
        while cur_abb != "A" and cur_abb != "R":
            rule_set = self.rules[cur_abb]
            print(cur_abb, rule_set)
            for rule in rule_set:
                if rule[0] == "":
                    cur_abb = rule[1]
                elif eval(rule[0]):
                    cur_abb = rule[1]
                    break
                else:
                    continue
        
        if cur_abb == "A":
            return True
        elif cur_abb == "R":
            return False