import math

class LowestCommonMultiple:

    def __init__(self):
        pass

    def calculate_lcm(self, steps):
        result = steps[0]
        for num in steps[1:]:
            result = self.lcm(result, num)
        return result


    def lcm(self, a, b):
        return abs(a * b) // math.gcd(a, b)