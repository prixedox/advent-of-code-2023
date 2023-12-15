from .AsciiSum import AsciiSum

class BoxSorter:

    def __init__(self):
        self.as_ = AsciiSum()
        self.boxes = [[] for _ in range(256)]

    def process(self, strings):
        for string in strings:
            if "-" in string:
                cur = string.replace("-", "")
                self.handle_dash(cur)
            elif "=" in string:
                cur = string.split("=")
                self.handle_equal(cur[0], int(cur[1]))

        self.print_boxes()

        sum_ = self.sum_boxes()
        return sum_
    
    def handle_dash(self, string):
        box_number = self.as_.get_ascii_sum(string)
        for elm in self.boxes[box_number]:
            if string in elm:
                self.boxes[box_number].remove(elm)

    def handle_equal(self, string, focal):
        box_number = self.as_.get_ascii_sum(string)
        appended = False
        for elm in self.boxes[box_number]:
            if elm[0] == string:
                elm[1] = focal
                appended = True
        
        if not appended:
            self.boxes[box_number].append([string, focal])

    def print_boxes(self):
        for i, box in enumerate(self.boxes):
            if box:
                print(i, box)

    def sum_boxes(self):
        sum_ = 0
        for i, box in enumerate(self.boxes):
            for j, elm in enumerate(box):
                sum_ += (i + 1) * (j + 1) * elm[1]

        return sum_