class Possibilities:

    def __init__(self):
        pass

    def extend(self, springs):
        extended_possibilities = []
        #spring = '???.###'
        for spring in springs:
        #print(spring)
            queue = [spring]
            i = 0
            while queue:
                #print(queue)
                i = 0
                spring = queue.pop(0)
                while i < len(spring):
                    if spring[i] == "?":
                        spring = spring[:i] + "." + spring[i+1:]
                        queue.append(spring)
                        spring = spring[:i] + "#" + spring[i+1:]
                        queue.append(spring)
                        #queue.pop(0)
                        break
                    i += 1
                
                if i == len(spring):
                    queue.append(spring)
                    extended_possibilities.append(queue)
                    print(len(queue))
                    break
                
        return extended_possibilities