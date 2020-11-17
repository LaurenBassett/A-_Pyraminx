# A-_Pyraminx

This code generates a Four-Level Pyraminx, shuffles it randomly, then solves it again using the A* Heuristic. 
It was completed for Dr. Goldsmith at the Univeristy of Kentucky in Fall 2020 for CS 463: Artificial Intelligence.  

This program has two object classes, Node and Pyraminx, and one general file. The program runs like this:
First, based on a given n random swaps, a pyraminx is generated and then randomly scrambled n times. 

The randomizer exists inside of a loop, which iterates for each swap requested by the user at the beginning of the program. In each iteration, a random number is generated. Because Python does not have switch statements, I use if/else statements in a similar format. Based on the random number generated, I call one of the 12 swap functions. This repeats for each swap designated by the user. To keep track of the swaps and check for errors, the swaps are entered into a file called “swaps.txt.”

***I do account for counter-clockwise swaps, the rotation algorithm is called twice in a row to swap it. I didn’t program it because I thought it would be a waste of time
. The user is shown an image of the shuffled pyraminx. **because the pyraminx is completely randomized, it may range from appearing to be very shuffled, or only slightly shuffled. While this does have an affect on the speed in which the program can solve the pyraminx, it is normal to see variations in the shuffles on the pyraminx. 
Once the pyraminx has been created and randomized, it is pushed into a heap, which starts the solving process of the program. 
The heap functions as follows: 

The first node is popped off the heap. 

The node is evaluated to see if the pyraminx has been solved. If it has, the program calculates the total cost by searching all parent nodes, and then prints the total cost and depth to the console, while generating an image of the solved pyraminx using the node to prove it has been solved. 
If the node does not contain the solution to the pyraminx, the following then occurs:
The program generates a pyraminx for each possible rotation of the pyraminx, and calculates the heuristic, and therefore the cost for each of them. The newly created nodes are then pushed into the heap using heap sort, and sorted by their total cost. Then the node with the lowest cost is popped out of the heap, and the cycle begins again. 
Data Structures: 

For my data structure, I generated an array that represented the “cubies” in each of the four sides of the pyraminx. I knew that even as the pyraminx shifted, each swap would involve the same parts of the pyraminx every single time. While the content (color) of the indices change, the specific indices exchanging data do not. 
Thus, I decided to model my arrays in this fashion, and kept my labeling constant in all functions of the program.  This was my original sketch. The numbering convention did not change. 
 
Heuristic: 

My heuristic is this: check the number of sides that are out of place, and divide that by four. This gives the number of swaps needed to align the sides of the pyraminx. 
 
