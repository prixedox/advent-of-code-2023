LOW = 0
HIGH = 1

class StateChanger:

    def __init__(self, lines):
        self.lines = lines
        self.states_flip = {}
        self.states_conj = {}
        self.init_states()
    
    def init_states(self):
        self.states_flip["button"] = LOW
        for line in self.lines:
            source_abb = line[1]
            if line[0] != "&" and source_abb not in self.states_flip:
                self.states_flip[source_abb] = LOW
        
        for line in self.lines:
            source_abb = line[1]
            if line[0] == "&":
                if source_abb not in self.states_conj:
                    self.states_conj[source_abb] = {}
                    for line2 in self.lines:
                        if source_abb in line2[2]:
                            self.states_conj[source_abb][line2[1]] = LOW
    
    def cycle(self):
        total = [0, 0]
        for _ in range(1000):
            sum_ = self.change_states()
            total[0] += sum_[0]
            total[1] += sum_[1]
        return total[0] * total[1]

    def change_states(self):
        queue = [("s", "button", ["roadcaster"])]
        pulses = [0, 0]
        while queue:
            #print("queue: ", queue)
            cur_line = queue.pop(0)
            source_abb = cur_line[1]
            source_type = cur_line[0]
            
            #print("line: ", cur_line)
            #print("source abb: ", source_abb)
            for target_abb in cur_line[2]:
                #print("target abb: ", target_abb)
                if source_type == "%":
                    source_state = self.states_flip[source_abb]
                    if target_abb in self.states_flip:
                        if source_state == LOW:
                            pulses[0] += 1
                            if self.states_flip[target_abb] == LOW:
                                self.states_flip[target_abb] = HIGH
                                queue.append(self.get_line_by_abb(target_abb))
                            else:
                                self.states_flip[target_abb] = LOW
                                queue.append(self.get_line_by_abb(target_abb))
                        else:
                            pulses[1] += 1
                            
                    elif target_abb in self.states_conj:
                        if source_state == LOW:
                            pulses[0] += 1
                        else:
                            pulses[1] += 1
                        queue.append(self.get_line_by_abb(target_abb))
                        self.states_conj[target_abb][source_abb] = source_state
                elif source_type == "&":
                    source_state = self.get_conj_state(source_abb)
                    if source_state == LOW:
                        pulses[0] += 1
                    else:
                        pulses[1] += 1
                    if target_abb in self.states_flip:
                        if source_state == LOW:
                            if self.states_flip[target_abb] == LOW:
                                self.states_flip[target_abb] = HIGH
                                queue.append(self.get_line_by_abb(target_abb))
                            else:
                                self.states_flip[target_abb] = LOW
                                queue.append(self.get_line_by_abb(target_abb))
                        else:
                            pass
                    elif target_abb in self.states_conj:
                        pass
                elif source_type == "s":
                    source_state = self.states_flip[source_abb]
                    if source_state == LOW:
                        pulses[0] += 1
                        queue.append(self.get_line_by_abb(target_abb))
                    else:
                        pulses[1] += 1

                elif source_type == "b":
                    source_state = self.states_flip[source_abb]
                    if target_abb in self.states_flip:
                        if source_state == LOW:
                            pulses[0] += 1
                            if self.states_flip[target_abb] == LOW:
                                self.states_flip[target_abb] = HIGH
                                queue.append(self.get_line_by_abb(target_abb))
                            else:
                                self.states_flip[target_abb] = LOW
                                queue.append(self.get_line_by_abb(target_abb))
                        else:
                            pulses[1] += 1
                            
                    elif target_abb in self.states_conj:
                        queue.append(self.get_line_by_abb(target_abb))
                        self.states_conj[target_abb][source_abb] = source_state
                
                #print("source state: ", source_state)
            #print("pulses: ", pulses)
            #print()
        
        #print(pulses)
        return pulses
    
    def get_line_by_abb(self, abb):
        for line in self.lines:
            if line[1] == abb:
                return line

    def get_conj_state(self, abb):
        vals = list(self.states_conj[abb].values())
        if sum(vals) == len(vals):
            return LOW
        else:
            return HIGH


        
        
    
    
            


