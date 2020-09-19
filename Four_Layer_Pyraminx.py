# Modeling the Pyraminx 
# Author: Lauren Bassett
# CS 463 -- Dr. Goldsmith
# Due September 4th
#-----------------------------
# Referenced: 
# (1) https://github.com/davidwhogg/MagicCube
# (2) https://ruwix.com/twisty-puzzles/pyraminx-triangle-rubiks-cube/master-pyraminx/
# (3) https://codereview.stackexchange.com/questions/197287/codefights-pyraminx-puzzle
# (4) https://ruwix.com/online-puzzle-simulators/pyraminx-simulator.php
# (5) https://pynative.com/python-random-randrange/
#-----------------------------
# Functions:
# Randomizer
# Face Operations 
# GUI/Print/Output
# Data Structure for Puzzle 
#------------------------------
# Deliverables: 
# Description of Data Structure
# Code and Instructions on how to run data structure 
# GUI output
# Description of Randomizer 
# Heuristic
# Statement of what I learned
#-------------------------------

#import statements 
#import pyraminx_class
from functools import partial 
from graphics import *
import random 
from functools import partial
import Pyraminx as pyraminx
import Node as node
import copy
import heapq
PERFECT_PYRA = pyraminx.Pyraminx()
def draw(R,G,B,Y):
    win = GraphWin("Pyraminx", 650, 500)
    R00Cord = [Point(125,50), Point(100, 100), Point(150,100)]
    R01Cord = [Point(100,100), Point(75, 150), Point(125,150)]
    R02Cord = [Point(100,100), Point(125, 150), Point(150,100)]
    R03Cord = [Point(125,150), Point(175, 150), Point(150,100)]
    R04Cord = [Point(50,200), Point(75, 150), Point(100,200)]
    R05Cord = [Point(75,150), Point(100, 200), Point(125,150)]
    R06Cord = [Point(100,200), Point(125, 150), Point(150,200)]
    R07Cord = [Point(125,150), Point(150, 200), Point(175,150)]
    R08Cord = [Point(150,200), Point(175, 150), Point(200,200)]
    R09Cord = [Point(25,250), Point(50, 200), Point(75,250)]
    R10Cord = [Point(50,200), Point(75, 250), Point(100,200)]
    R11Cord = [Point(75,250), Point(100, 200), Point(125,250)]
    R12Cord = [Point(100,200), Point(125, 250), Point(150,200)]
    R13Cord = [Point(125,250), Point(150, 200), Point(175,250)]
    R14Cord = [Point(150,200), Point(175, 250), Point(200,200)]
    R15Cord = [Point(175,250), Point(200, 200), Point(225,250)]
    B00Cord = [Point(525,50), Point(500, 100), Point(550,100)]
    B01Cord = [Point(475,150), Point(500, 100), Point(525,150)]
    B02Cord = [Point(500,100), Point(525, 150), Point(550,100)]
    B03Cord = [Point(525,150), Point(575, 150), Point(550,100)]
    B04Cord = [Point(450,200), Point(475, 150), Point(500,200)]
    B05Cord = [Point(475,150), Point(500, 200), Point(525,150)]
    B06Cord = [Point(500,200), Point(525, 150), Point(550,200)]
    B07Cord = [Point(525,150), Point(550, 200), Point(575,150)]
    B08Cord = [Point(550,200), Point(575, 150), Point(600,200)]
    B09Cord = [Point(425,250), Point(450, 200), Point(475,250)]
    B10Cord = [Point(450,200), Point(475, 250), Point(500,200)]
    B11Cord = [Point(475,250), Point(500, 200), Point(525,250)]
    B12Cord = [Point(500,200), Point(525, 250), Point(550,200)]
    B13Cord = [Point(525,250), Point(550, 200), Point(575,250)]
    B14Cord = [Point(550,200), Point(575, 250), Point(600,200)]
    B15Cord = [Point(575,250), Point(600, 200), Point(625,250)]
    G00Cord = [Point(325,50), Point(300, 100), Point(350,100)]
    G01Cord = [Point(275,150), Point(300, 100), Point(325,150)]
    G02Cord = [Point(300,100), Point(325, 150), Point(350,100)]
    G03Cord = [Point(325,150), Point(375, 150), Point(350,100)]
    G04Cord = [Point(250,200), Point(275, 150), Point(300,200)]
    G05Cord = [Point(275,150), Point(300, 200), Point(325,150)]
    G06Cord = [Point(300,200), Point(325, 150), Point(350,200)]
    G07Cord = [Point(325,150), Point(350, 200), Point(375,150)]
    G08Cord = [Point(350,200), Point(375, 150), Point(400,200)]
    G09Cord = [Point(225,250), Point(250, 200), Point(275,250)]
    G10Cord = [Point(250,200), Point(275, 250), Point(300,200)]
    G11Cord = [Point(275,250), Point(300, 200), Point(325,250)]
    G12Cord = [Point(300,200), Point(325, 250), Point(350,200)]
    G13Cord = [Point(325,250), Point(350, 200), Point(375,250)]
    G14Cord = [Point(350,200), Point(375, 250), Point(400,200)]
    G15Cord = [Point(375,250), Point(400, 200), Point(425,250)]
    Y00Cord = [Point(325,460), Point(300, 410), Point(350,410)]
    Y01Cord = [Point(275,360), Point(300, 410), Point(325,360)]
    Y02Cord = [Point(300,410), Point(325, 360), Point(350,410)]
    Y03Cord = [Point(325,360), Point(375, 360), Point(350,410)]
    Y04Cord = [Point(250,310), Point(275, 360), Point(300,310)]
    Y05Cord = [Point(275,360), Point(300, 310), Point(325,360)]
    Y06Cord = [Point(300,310), Point(325, 360), Point(350,310)]
    Y07Cord = [Point(325,360), Point(350, 310), Point(375,360)]
    Y08Cord = [Point(350,310), Point(375, 360), Point(400,310)]
    Y09Cord = [Point(225,260), Point(250, 310), Point(275,260)]
    Y10Cord = [Point(250,310), Point(275, 260), Point(300,310)]
    Y11Cord = [Point(275,260), Point(300, 310), Point(325,260)]
    Y12Cord = [Point(300,310), Point(325, 260), Point(350,310)]
    Y13Cord = [Point(325,260), Point(350, 310), Point(375,260)]
    Y14Cord = [Point(350,310), Point(375, 260), Point(400,310)]
    Y15Cord = [Point(375,260), Point(400, 310), Point(425,260)]
    Y00 = Polygon(Y00Cord)
    Y00.setFill(Y[0])
    Y00.draw(win)
    Y01 = Polygon(Y01Cord)
    Y01.setFill(Y[1])
    Y01.draw(win)
    Y02 = Polygon(Y02Cord)
    Y02.setFill(Y[2])
    Y02.draw(win)
    Y03 = Polygon(Y03Cord)
    Y03.setFill(Y[3])
    Y03.draw(win)
    Y04 = Polygon(Y04Cord)
    Y04.setFill(Y[4])
    Y04.draw(win)
    Y05 = Polygon(Y05Cord)
    Y05.setFill(Y[5])
    Y05.draw(win)
    Y06 = Polygon(Y06Cord)
    Y06.setFill(Y[6])
    Y06.draw(win)
    Y07 = Polygon(Y07Cord)
    Y07.setFill(Y[7])
    Y07.draw(win)
    Y08 = Polygon(Y08Cord)
    Y08.setFill(Y[8])
    Y08.draw(win)
    Y09 = Polygon(Y09Cord)
    Y09.setFill(Y[9])
    Y09.draw(win)
    Y10 = Polygon(Y10Cord)
    Y10.setFill(Y[10])
    Y10.draw(win)
    Y11 = Polygon(Y11Cord)
    Y11.setFill(Y[11])
    Y11.draw(win)
    Y12 = Polygon(Y12Cord)
    Y12.setFill(Y[12])
    Y12.draw(win)
    Y13 = Polygon(Y13Cord)
    Y13.setFill(Y[13])
    Y13.draw(win)
    Y14 = Polygon(Y14Cord)
    Y14.setFill(Y[14])
    Y14.draw(win)
    Y15 = Polygon(Y15Cord)
    Y15.setFill(Y[15])
    Y15.draw(win) 
    G00 = Polygon(G00Cord)
    G00.setFill(G[0])
    G00.draw(win)
    G01 = Polygon(G01Cord)
    G01.setFill(G[1])
    G01.draw(win)
    G02 = Polygon(G02Cord)
    G02.setFill(G[2])
    G02.draw(win)
    G03 = Polygon(G03Cord)
    G03.setFill(G[3])
    G03.draw(win)
    G04 = Polygon(G04Cord)
    G04.setFill(G[4])
    G04.draw(win)
    G05 = Polygon(G05Cord)
    G05.setFill(G[5])
    G05.draw(win)
    G06 = Polygon(G06Cord)
    G06.setFill(G[6])
    G06.draw(win)
    G07 = Polygon(G07Cord)
    G07.setFill(G[7])
    G07.draw(win)
    G08 = Polygon(G08Cord)
    G08.setFill(G[8])
    G08.draw(win)
    G09 = Polygon(G09Cord)
    G09.setFill(G[9])
    G09.draw(win)
    G10 = Polygon(G10Cord)
    G10.setFill(G[10])
    G10.draw(win)
    G11 = Polygon(G11Cord)
    G11.setFill(G[11])
    G11.draw(win)
    G12 = Polygon(G12Cord)
    G12.setFill(G[12])
    G12.draw(win)
    G13 = Polygon(G13Cord)
    G13.setFill(G[13])
    G13.draw(win)
    G14 = Polygon(G14Cord)
    G14.setFill(G[14])
    G14.draw(win)
    G15 = Polygon(G15Cord)
    G15.setFill(G[15])
    G15.draw(win) 
    B00 = Polygon(B00Cord)
    B00.setFill(B[0])
    B00.draw(win)
    B01 = Polygon(B01Cord)
    B01.setFill(B[1])
    B01.draw(win)
    B02 = Polygon(B02Cord)
    B02.setFill(B[2])
    B02.draw(win)
    B03 = Polygon(B03Cord)
    B03.setFill(B[3])
    B03.draw(win)
    B04 = Polygon(B04Cord)
    B04.setFill(B[4])
    B04.draw(win)
    B05 = Polygon(B05Cord)
    B05.setFill(B[5])
    B05.draw(win)
    B06 = Polygon(B06Cord)
    B06.setFill(B[6])
    B06.draw(win)
    B07 = Polygon(B07Cord)
    B07.setFill(B[7])
    B07.draw(win)
    B08 = Polygon(B08Cord)
    B08.setFill(B[8])
    B08.draw(win)
    B09 = Polygon(B09Cord)
    B09.setFill(B[9])
    B09.draw(win)
    B10 = Polygon(B10Cord)
    B10.setFill(B[10])
    B10.draw(win)
    B11 = Polygon(B11Cord)
    B11.setFill(B[11])
    B11.draw(win)
    B12 = Polygon(B12Cord)
    B12.setFill(B[12])
    B12.draw(win)
    B13 = Polygon(B13Cord)
    B13.setFill(B[13])
    B13.draw(win)
    B14 = Polygon(B14Cord)
    B14.setFill(B[14])
    B14.draw(win)
    B15 = Polygon(B15Cord)
    B15.setFill(B[15])
    B15.draw(win) 
    R00 = Polygon(R00Cord)
    R00.setFill(R[0])
    R00.draw(win)
    R01 = Polygon(R01Cord)
    R01.setFill(R[1])
    R01.draw(win)
    R02 = Polygon(R02Cord)
    R02.setFill(R[2])
    R02.draw(win)
    R03 = Polygon(R03Cord)
    R03.setFill(R[3])
    R03.draw(win)
    R04 = Polygon(R04Cord)
    R04.setFill(R[4])
    R04.draw(win)
    R05 = Polygon(R05Cord)
    R05.setFill(R[5])
    R05.draw(win)
    R06 = Polygon(R06Cord)
    R06.setFill(R[6])
    R06.draw(win)
    R07 = Polygon(R07Cord)
    R07.setFill(R[7])
    R07.draw(win)
    R08 = Polygon(R08Cord)
    R08.setFill(R[8])
    R08.draw(win)
    R09 = Polygon(R09Cord)
    R09.setFill(R[9])
    R09.draw(win)
    R10 = Polygon(R10Cord)
    R10.setFill(R[10])
    R10.draw(win)
    R11 = Polygon(R11Cord)
    R11.setFill(R[11])
    R11.draw(win)
    R12 = Polygon(R12Cord)
    R12.setFill(R[12])
    R12.draw(win)
    R13 = Polygon(R13Cord)
    R13.setFill(R[13])
    R13.draw(win)
    R14 = Polygon(R14Cord)
    R14.setFill(R[14])
    R14.draw(win)
    R15 = Polygon(R15Cord)
    R15.setFill(R[15])
    R15.draw(win) 
    win.getMouse()
    #  win.getMouse()
    win.close()

"""def find_heuristic(R,G,B,Y):
    R_count = side(R, 'red')
    G_count = side(G, 'green')
    B_count = side(B, 'blue')
    Y_count = side(Y, 'yellow')
    total = ((R_count + G_count + B_count + Y_count) / 3)
    return total"""
def find_child(pyra):
  
    temp_heur = 999999999
    nodes = []
    #-----Check u/U/Uw
    u = node.Node(0,pyra)
    u.pyra = copy.deepcopy(pyra)
    u.pyra.u_swap()
    u.heuristic = u.find_heuristic()
    
    heapq.heappush(nodes,u)
    U = node.Node(0,pyra)
    U.pyra = copy.deepcopy(pyra)
    U.pyra.U_swap()
    U.heuristic = U.find_heuristic()
    #print("U heuristic is ", U.heuristic)
    heapq.heappush(nodes,U)
   
    Uw = node.Node(0,pyra)
    Uw.pyra = copy.deepcopy(pyra)
    Uw.pyra.Uw_swap()
    Uw.heuristic = Uw.find_heuristic()
    # print("Uw heuristic is ", Uw.heuristic)
    heapq.heappush(nodes, Uw)
      
    b = node.Node(0,pyra)
    b.pyra = copy.deepcopy(pyra)
    b.pyra.b_swap()
    b.heuristic = b.find_heuristic()
    #print("b heuristic is ", b.heuristic)
    heapq.heappush(nodes, b)
   
    B = node.Node(0,pyra)
    B.pyra = copy.deepcopy(pyra)
    B.pyra.B_swap()
    B.heuristic = B.find_heuristic()
    #print("B heuristic is ", B.heuristic)
    heapq.heappush(nodes, B)

    Bw = node.Node(0,pyra)
    Bw.pyra = copy.deepcopy(pyra)
    Bw.pyra.Bw_swap()
    Bw.heuristic = Bw.find_heuristic()
    #print("Bw heuristic is ", Bw.heuristic)
    heapq.heappush(nodes, Bw)
  
    L = node.Node(0,pyra)
    L.pyra = copy.deepcopy(pyra)
    L.pyra.L_swap()
    L.heuristic = L.find_heuristic()
    #print("L heuristic is ", L.heuristic)
    heapq.heappush(nodes, L)
    l = node.Node(0,pyra)
    l.pyra = copy.deepcopy(pyra)
    l.pyra.l_swap()
    l.heuristic = l.find_heuristic()
    #print("l heuristic is ", l.heuristic)
    heapq.heappush(nodes, l)
    Lw = node.Node(0,pyra)
    Lw.pyra = copy.deepcopy(pyra)
    Lw.pyra.Lw_swap()
    Lw.heuristic = Lw.find_heuristic()
    #print("Lw heuristic is ", Lw.heuristic)
    heapq.heappush(nodes, Lw)
       
    r = node.Node(0,pyra)
    r.pyra = copy.deepcopy(pyra)
    r.pyra.r_swap()
    r.heuristic = r.find_heuristic()
    #print("r heuristic is ", r.heuristic)
    heapq.heappush(nodes, r)

    R = node.Node(0,pyra)
    R.pyra = copy.deepcopy(pyra)
    R.pyra.R_swap()
    R.heuristic = R.find_heuristic()
    #print("R heuristic is ", R.heuristic)
    heapq.heappush(nodes, R)

    Rw = node.Node(0,pyra)
    Rw.pyra = copy.deepcopy(pyra)
    Rw.pyra.Rw_swap()
    Rw.heuristic = Rw.find_heuristic()
    #print("Rw heuristic is ", Rw.heuristic)
    heapq.heappush(nodes, Rw)
    
    return nodes
    
def isPerfect(pyra):
    if(pyra.R == PERFECT_PYRA.R and pyra.G == PERFECT_PYRA.G and pyra.B == PERFECT_PYRA.B and pyra.Y == PERFECT_PYRA.Y):
        return True
    else:
        return False
def main():
    possible_solves =[]
    heapq.heapify(possible_solves)
    p = pyraminx.Pyraminx()
    n = 4
    #draw(p.R, p.G, p.B, p.Y)
    i = 0
    while (i < n):
        p.randomize()
        i= i+1
    draw(p.R, p.G, p.B, p.Y)
    
    #initial: 
    
    #p is my randomized pyraminx and now I need to solve it
    first_node = node.Node(0, p)
    first_node.pyra = p
    currNode = copy.deepcopy(first_node)
    heapq.heappush(possible_solves, currNode)
    
    while possible_solves:
        #pop node from heap
        current = node.Node(0,p)
        current = heapq.heappop(possible_solves)
        if (isPerfect(current.pyra)):
            draw(current.pyra.R, current.pyra.G, current.pyra.B, current.pyra.Y)
            quit
        children = find_child(current.pyra)
        for item in children:
            current.child = item
            item.parent = current   
            item.cost = current.cost + 1
            item.depth = current.depth + 1
            heapq.heappush(possible_solves, item)
        
        #draw(current.pyra.R, current.pyra.G, current.pyra.B, current.pyra.Y)
        #if node is answer, exit 
        #else expand children and calculate heuristic and cost
        #add children to the heap 
    #while (isPerfect(currNode.pyra) == False):
    
    #draw(currNode.pyra.R, currNode.pyra.G, currNode.pyra.B, currNode.pyra.Y)
main()

