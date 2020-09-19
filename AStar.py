#---------------Modeling A*---------------#
# Pre Conditions: Four Randomized Arrays 
# Post Conditions: A Sorted Pyraminx 
# Referenced: https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb

#Heuristic given by Will Berry 
#Heuristic: The edge pieces (except corners) that are out of place divded by 4

QUEUE = [] #Queue to store list modeling pyraminx throughout program 

import Pyraminx as pyraminx
import Node as node
import copy.deepcopy as dcpy
import heapq

def main():
    #Get Randomized Arrays
    #Turn Arrays into Node 
    #----------------------------------------------------------------------------------
    # A* Definitions
    #----------------------------------------------------------------------------------
    # node(self, depth, pyraminx):
   
    #goal node <- where to stop searching
    #search space <- a collection of nodes, like all board positions of a board game
    #cost  <- numerical value for the path from a node to another node
    myPyraminx = pyraminx.Pyraminx()
    myPyraminx.randomize()
    n = node.Node(0,pyraminx)
    
    #solver
    #initiate with heap
    #while heap is not empty, remove from queue and generate heuristic, if correct good
    #if false generate children and heuristic for those 
    #expand out 
    #calculate cost of children 
    
    #three functions 

    #heap() <- one node 

    #expand() <-every time I make a child I make one of every new pyraminx 
    
    #put a node on the q
    #take it off qu

    heapq.heappop(QUEUE)
    heapq.heappush(QUEUE, node) #add node to heap 
main();

