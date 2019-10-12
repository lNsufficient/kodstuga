import random

class Board(object):
    def __init__():
        board_list = [0]*40
        current_position = 0

    def get_next_dice():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1+d2   

    def walk(self):
        steps = self.get_next_dice()
        self.current_position = self.get_next_position(steps)
        self.current_position = self.take_action()
        self.board_list[self.current_position] = self.board_list[self.current_position] + 1

