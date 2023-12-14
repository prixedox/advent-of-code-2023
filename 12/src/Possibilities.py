from functools import cache


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
    
    @cache
    def count_configs(self, spring, nums):
        if spring == "":
            if nums == ():
                return 1
            else:
                return 0
        
        if nums == ():
            if "#" not in spring:
                return 1
            else:
                return 0
        
        result = 0

        if spring[0] in ".?":
            result += self.count_configs(spring[1:], nums)
        
        if spring[0] in "#?":
            if nums[0] <= len(spring) and "." not in spring[:nums[0]] and (nums[0] == len(spring) or spring[nums[0]] != "#"):
                result += self.count_configs(spring[nums[0] + 1:], nums[1:])
            else:
                result += 0

        return result

    
    def get_number_of_possibilities(self, springs, numbers):
        sum_ = 0
        for i in range(len(springs)):
            nums = tuple(numbers[i])
            nums *= 5
            spring = "?".join([springs[i]] * 5)

            sum_ += self.count_configs(spring, nums)
        return sum_
