import random
import sys

class Deck(object):
    def __init__(self, nbr_cards, list_of_tiles):
        self.nbr_cards = nbr_cards
        self.a = list_of_tiles + [""]*(nbr_cards-len(list_of_tiles))
        random.shuffle(self.a)
        self.position = 0

    def pop(self):
        #We are ok with not starting with top card but second card
        self.position = (self.position + 1)%self.nbr_cards
        return self.a[self.position]

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
        self.cc_deck = Deck(16, ["JAIL", "GO"])
        self.ch_deck = Deck(16, ["GO", "JAIL", "C1", "E3", "H2", "R1", "NEXTR", "NEXTR", "NEXTU", "BACK3"])
        self.double_count = 0

    @staticmethod
    def roll_dice():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1, d2

    def get_next_dice(self):
        d1, d2 = Board.roll_dice()
        steps = d1 + d2
        if (d1 == d2):
            self.double_count += 1
            if self.double_count > 2:
                return -1
        else:
            self.double_count = 0
        return steps   

    def get_next_position(self, steps):
        next_position = (self.current_position + steps)%self.board_len
        return next_position

    def goto(self, s):
        if s == "":
            new_position = self.current_position
        elif s == "NEXTR":
            new_position = self.get_next_('R')
        elif s == "NEXTU":
            new_position = self.get_next_('U')
        elif s == "BACK3":
            new_position = ((self.current_position - 3)+self.board_len)%self.board_len
        else:
            new_position = self.board_tiles.index(s)
        self.current_position = new_position
    
    def get_positions_starting_w(self, s):
        return [e for e in range(self.board_len) if self.board_tiles[e][0] == s] 
 
    def get_next_(self, S):
        v = self.get_positions_starting_w(S)
        new_pos_v = [e for e in v if e < self.current_position]
        if len(new_pos_v) == 0:
            new_pos = v[0]
        else:
            new_pos = new_pos_v[0]
        return new_pos

    def take_cc(self):
        #returns new position tile
        new_tile = self.cc_deck.pop()
        return new_tile

    def take_ch(self):
        #returns new position tile
        new_tile = self.ch_deck.pop()
        return new_tile

    def take_action(self):
        tile = self.board_tiles[self.current_position]
        if tile == "G2J":
            new_tile = "JAIL"
        elif tile[0:2] == "CC":
            new_tile = (self.take_cc())
        elif tile[0:2] == "CH":
            new_tile = (self.take_ch())
        else:
            new_tile = tile
        self.goto(new_tile)

    def walk(self):
        steps = self.get_next_dice()
        if steps == -1:
            self.goto("JAIL")
        else:
            self.current_position = self.get_next_position(steps)
            self.take_action()
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
