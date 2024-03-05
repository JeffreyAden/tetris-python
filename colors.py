
class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (46, 46, 127)
    light_blue = (59, 85, 162)

    # add a list of 8 colors that'll be used for the tetris blocks
    # use a decorator to access attributes of the class

    @classmethod
    def get_cell_colors(cls): # "self "allows obj level access while "cls "allows class level access
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
    # the order of the colors is key so keep it in mind
