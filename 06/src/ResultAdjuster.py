class ResultAdjuster:

    def __init__(self):
        pass

    def multiply_array(self, array):
        mult = 1
        for item in array:
            mult *= item
        return mult