class Filter:

    def __init__(self, rules, parts):
        self.rules = rules
        self.parts = parts

    def filter_parts(self):
        sum_ = 0
        for part in self.parts:
            is_accepted = self.filter_single(part)
            if is_accepted:
                sum_ += self.sum_parts(part)
                
        return sum_
    
    def filter_single(self, part):
        x = part["x"]
        m = part["m"]
        a = part["a"]
        s = part["s"]
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
    
    def sum_parts(self, part):
        x = part["x"]
        m = part["m"]
        a = part["a"]
        s = part["s"]
        return x + m + a + s