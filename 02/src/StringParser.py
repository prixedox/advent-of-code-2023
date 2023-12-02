class StringParser:

    def __init__(self):
        self.games = []

    def get_max_amount_in_game(self, string_array):
        for string in string_array:
            set_split = self.split_by_set(string)
            color_split = self.split_by_color(set_split)
            rgb_max = self.get_max_color(color_split)
            self.games.append(rgb_max)
        return self.games

    def split_by_set(self, string: str):
        set_split = string.split(":")[1].split(";")

        return set_split

    def split_by_color(self, sets: list):
        set_color = []
        for game_set in sets:
            items = game_set.split(",")
            color = []
            for item in items:
                item = item.strip()
                color.append(item)
            set_color.append(color)

        return set_color

    def get_max_color(self, color_split):
        rgb_max = [0, 0, 0]
        for game_set in color_split:
            for item in game_set:
                count_color = item.split(" ")
                count = int(count_color[0])
                if count_color[1] == "red":
                    if count > rgb_max[0]:
                        rgb_max[0] = count
                elif count_color[1] == "green":
                    if count > rgb_max[1]:
                        rgb_max[1] = count
                elif count_color[1] == "blue":
                    if count > rgb_max[2]:
                        rgb_max[2] = count

        return rgb_max
