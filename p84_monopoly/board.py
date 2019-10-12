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

    def goto(self, s):
        return self.board_tiles.index(s)

    def take_cc(self, position):
        #returns new position tile
        return self.board_tiles[position]

    def take_ch(self, position):
        #returns new position tile
        return self.board_tiles[position]

    def take_action(self, position):
        tile = self.board_tiles[position]
        if tile == "G2J":
            new_position = self.goto("JAIL")
        elif tile[0:2] == "CC":
            new_position = self.goto(self.take_cc(position))
        elif tile[0:2] == "CH":
            new_position = self.goto(self.take_ch(position))
        else:
            new_position = position
        return new_position

    def walk(self):
        steps = Board.get_next_dice()
        self.current_position = self.get_next_position(steps)
        self.current_position = self.take_action(self.current_position)
        self.board_list[self.current_position] = self.board_list[self.current_position] + 1
        self.round += 1

    def __str__(self):
        rep = "Board status\n"
        l = [e/self.round for e in self.board_list]
        tuple_list = zip(self.board_tiles, l)
        for i, t in enumerate(tuple_list):
            if i%10==1:
                rep += '\n'
            rep += str(t)
        return rep

if __name__ == "__main__":
    b = Board()
    rounds = int(sys.argv[1])
    while(b.round < rounds):
        b.walk()
    print(b)
