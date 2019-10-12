import random
import sys

class Board(object):
    def __init__(self):
        self.board_list = [0]*40
        self.current_position = 0
        self.board_len = len(self.board_list)
        self.round = 0
        self.board_tiles = [
                "GO", "A1", "CC1","A2", "T1","R1", "B1", "CH1", "B2", "B3", 
                "JAIL","C1","U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", 
                "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
                "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
                ]                

    @staticmethod
    def get_next_dice():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1+d2   

    def get_next_position(self, steps):
        next_position = (self.current_position + steps)%self.board_len
        return next_position

    def take_action(self):
        return self.current_position

    def walk(self):
        steps = Board.get_next_dice()
        self.current_position = self.get_next_position(steps)
        self.current_position = self.take_action()
        self.board_list[self.current_position] = self.board_list[self.current_position] + 1
        self.round += 1

    def __str__(self):
        rep = "Board status\n"
        l = [e/self.round for e in self.board_list]
        rep += str(l)
        return rep

if __name__ == "__main__":
    b = Board()
    rounds = int(sys.argv[1])
    while(b.round < rounds):
        b.walk()
    print(b)
