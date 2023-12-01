from src.FileReader import FileReader
from src.StringParser import StringParser
from src.NumberHandler import NumberHandler

#FILENAME = "input-sm.txt"
#FILENAME = "input-sm2.txt"
FILENAME = "input.txt"
#FILENAME = "test.txt"

PART_TWO = False

def main():
    fr = FileReader(FILENAME)
    string_array = fr.get_string_array()
    sp = StringParser()
    numbers_string_array = sp.get_first_and_last_numbers(string_array, PART_TWO)
    nh = NumberHandler()
    result = nh.make_sum(numbers_string_array)
    print(result) #part 1 = 54951, part 2 = 55218

main()