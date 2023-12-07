import os

class FileReader():

    def __init__(self, filename):
        self.file_path = self.__get_file_from_parent_folder(filename)
    
    def __get_file_from_parent_folder(self, filename) -> str:
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        return os.path.join(parent_dir, filename)

    def get_string_array(self):
        string_array = []
        with open(self.file_path, 'r') as f:
            string_array = f.readlines()
        
        string_array_strip = []
        for string in string_array:
            string_array_strip.append(string.strip())
        return string_array_strip