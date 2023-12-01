class NumberHandler:

    def __init__(self):
        pass

    def make_sum(self, string_array) -> int:
        number_array = self.__to_number_array(string_array)
        sum_ = sum(number_array)

        return sum_
    

    def __to_number_array(self, string_array: list) -> list:
        number_array: list = []
        for string in string_array:
            number_array.append(int(string))
        
        return number_array