class AsciiSum:

    def __init__(self):
        pass

    def get_sum_of_strings(self, strings):
        total = 0
        for string in strings:
            total += self.get_ascii_sum(string)

        return total

    def get_ascii_sum(self, string):
        sum_ = 0
        for char in string:
            sum_ += ord(char)
            sum_ *= 17
            sum_ = sum_ % 256
        
        return sum_