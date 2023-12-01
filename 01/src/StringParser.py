TEXT_NUMBERS = {"one":"1",
                "two":"2",
                "three":"3",
                "four":"4",
                "five":"5",
                "six":"6",
                "seven":"7",
                "eight":"8",
                "nine":"9",
                }


class StringParser:

    def __init__(self):
        pass

    
    def get_first_and_last_numbers(self, string_array: list, extract_text: bool) -> list:
        numbers_string_array: list = []
        for string in string_array:
            if not extract_text:
                # part 1
                numbers_string = self.__extract_numbers(string)
            else:
                # part 2
                numbers_string = self.__extract_text_numbers(string)
            
            first_last = numbers_string[0] + numbers_string[-1]
            numbers_string_array.append(first_last)
        
        return numbers_string_array

    def __extract_numbers(self, string: str) -> str:
        numbers_string: str = ""
        for char in string:
            if char.isdigit():
                numbers_string += char
        
        return numbers_string

    def __extract_text_numbers(self, string: str) -> str:
        numbers = []
        for i in range(len(string)):
            if string[i].isdigit():
                numbers.append(string[i])
            for key in TEXT_NUMBERS:
                start_index = i-len(key)+1
                if start_index < 0:
                    continue
                if key == string[start_index:i+1]:
                    numbers.append(TEXT_NUMBERS[key])

        return "".join(numbers)
            