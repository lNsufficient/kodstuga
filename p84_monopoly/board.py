import random

class Board(object):
    def __init__(self):
        self.board_list = [0]*40
        self.current_position = 0
        self.board_len = len(self.board_list)

    @staticmethod
    def get_next_dice():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1+d2   

    def get_next_position(self, steps):
        next_position = (self.current_position + steps)%self.board_len
        return next_position

    def take_action():
        return self.current_position

    def walk(self):
        steps = Board.get_next_dice()
        self.current_position = self.get_next_position(steps)
        self.current_position = self.take_action()
        self.board_list[self.current_position] = self.board_list[self.current_position] + 1

