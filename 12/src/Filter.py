class Filter:

    def __init__(self):
        pass

    def filter(self, pos_springs, numbers):
        #print(numbers)
        #print(pos_springs)
        total_pos = 0
        for i in range(len(numbers)):
            print(i)
            for spring in pos_springs[i]:
                #print(spring)
                arr = []
                sum_ = 0
                was_hash = False
                for char in spring:
                    if char == ".":
                        if was_hash:
                            arr.append(sum_)
                        sum_ = 0
                        was_hash = False
                    elif char == "#":
                        was_hash = True
                        sum_ += 1
                if was_hash:
                    arr.append(sum_)
                    
                if arr == numbers[i]:
                    total_pos += 1
        return total_pos