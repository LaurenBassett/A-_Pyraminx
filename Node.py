import Pyraminx as pyraminx
import copy
QUEUE = [] 
SOLVEDPYRAMINX = pyraminx.Pyraminx()

class Node: 
    def __init__(self, depth, pyra):
        self.pyra = pyraminx.Pyraminx()
        self.depth = depth + 1
        self.heuristic = -1
        self.parent = None
        self.child = None
        self.cost = 0

    def __lt__(self, other):
       #return self.cost < other.cost
       return self.heuristic < other.heuristic

    def find_heuristic(self):
        def side(S, color):
            count = 0
            if S[1] != color:
                count = count + 1
            #if S[5] != color:
               # count = count + 1
            if S[4] != color:
                count = count + 1
            #if S[10] != color:
                #count = count + 1
            if S[3] != color:
                count = count + 1
            #if S[7] != color:
                #count = count + 1
            if S[8] != color:
                count = count + 1
            #if S[14] != color:
                # count = count + 1
            if S[11] != color:
                count = count + 1
            #if S[12] != color:
                #   count = count + 1
            if S[13] != color:
                count = count + 1
            return count 
            #return self.count 

        self.R_count = side(self.pyra.R, 'red')
        self.G_count = side(self.pyra.G, 'green')
        self.B_count = side(self.pyra.B, 'blue')
        self.Y_count = side(self.pyra.Y, 'yellow')
        self.total = ((self.R_count + self.G_count + self.B_count + self.Y_count) / 3)
        return self.total
  