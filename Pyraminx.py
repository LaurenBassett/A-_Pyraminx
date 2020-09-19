import random 

class Pyraminx:
    def __init__(self):
        self.R = ['red','red','red','red','red','red','red','red','red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
        self.G= ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
        self.B = ['blue', 'blue',  'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
        self.Y = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow' ]
        
    def u_swap(self):
        temp =[0,0]
        temp[0] = self.R[0]
        self.R[0] = self.G[0]
        self.G[0] = self.B[0]
        self.B[0] = temp[0]
    def U_swap(self):
       
        temp = [0,0,0,0,0]
        temp[0:4] = self.R[0:4]
        self.R[1] = self.G[1]
        self.R[2] = self.G[2]
        self.R[3] = self.G[3]
        self.G[1] = self.B[1]
        self.G[2] = self.B[2]
        self.G[3] = self.B[3]
        self.B[1] = temp[1]
        self.B[2] = temp[2]
        self.B[3] = temp[3]
    def Uw_swap(self):
       
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.R[0:16]
        self.R[5] = self.G[5]
        self.R[6] = self.G[6]
        self.R[7] = self.G[7]
        self.R[8] = self.G[8]
        self.R[4] = self.G[4]
        self.G[5] = self.B[5]
        self.G[6] = self.B[6]
        self.G[7]=  self.B[7]
        self.G[8] = self.B[8]
        self.G[4] = self.B[4]
        self.B[5] = temp[5]
        self.B[6] = temp[6]
        self.B[7] = temp[7]
        self.B[8] = temp[8]
        self.B[4] = temp[4]

    #----------------------L SWAPS---------------------------#
    def l_swap(self):
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[15]=self.R[15]
        self.R[15] = self.Y[9]
        self.Y[9] = self.G[9]
        self.G[9] = temp[15]
    def L_swap(self):
       
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.R[0:16]


        self.R[8] = self.Y[4]
        self.R[14] = self.Y[10]
        self.R[13] = self.Y[11]

        self.Y[4] = self.G[11]
        self.Y[10] = self.G[10]
        self.Y[11] = self.G[4]
        
        self.G[4] = temp[13]
        self.G[10] = temp[14]
        self.G[11] = temp[8]
    def Lw_swap(self):
        
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.R[0:16]
        self.R[3] = self.Y[1]
        self.R[7] = self.Y[5]
        self.R[6] = self.Y[6]
        self.R[12] = self.Y[12]
        self.R[11]=self.Y[13]

        self.Y[1] = self.G[13]
        self.Y[5] = self.G[12]
        self.Y[6] = self.G[6]
        self.Y[12] = self.G[5]
        self.Y[13] = self.G[1]

        self.G[1] = temp[11]
        self.G[5] = temp[12]
        self.G[6] = temp[6]
        self.G[12] = temp[7]
        self.G[13] = temp[3]
    #----------------------self.R SWAPS---------------------------#
    def r_swap(self):
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[15]=self.G[15]
        self.G[15] = self.Y[15]
        self.Y[15] = self.B[9]
        self.B[9] = temp[15]
    def R_swap(self):
        
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.G[0:16]
        self.G[8] = self.Y[13]
        self.G[13] = self.Y[8]
        self.G[14] = self.Y[14]
        
        self.Y[8]  =self.B[11]
        self.Y[13] = self.B[4]
        self.Y[14] = self.B[10]

        self.B[4] = temp[13]
        self.B[10] = temp[14]
        self.B[11] = temp[8]
    def Rw_swap(self):
        
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.G[0:16]

        self.G[3] =self.Y[11]
        self.G[7] = self.Y[12]
        self.G[6] = self.Y[6]
        self.G[12] = self.Y[7]
        self.G[11] = self.Y[3] 
        
        self.Y[11] = self.B[13]
        self.Y[12] = self.B[12]
        self.Y[6] = self.B[6]
        self.Y[7] = self.B[5]
        self.Y[3] = self.B[1]
        
        self.B[1] = temp[11]
        self.B[5] = temp[12]
        self.B[6] =temp[6]
        self.B[12] = temp[7]
        self.B[13] = temp[3]
        
    #----------------------self.B SWAPS---------------------------#
    def b_swap(self):
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[9]=self.R[9]
        self.R[9] = self.B[15]
        self.B[15] = self.Y[0]
        self.Y[0] = temp[9]
    def B_swap(self):
       
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.R[0:16]
        self.R[4] = self.B[13] 
        self.R[10] = self.B[14]
        self.R[11] = self.B[8]

        self.B[8] = self.Y[3]
        self.B[13] = self.Y[1]
        self.B[14]= self.Y[2]

        self.Y[1] = temp[4]
        self.Y[2] = temp[10]
        self.Y[3] = temp[11]
    def Bw_swap(self):
        
        temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        temp[0:16] = self.R[0:16]
        self.R[1] = self.B[11]
        self.R[5] = self.B[12]
        self.R[6] =self.B[6]
        self.R[12] = self.B[7]
        self.R[13] =self.B[3]

        self.B[3] = self.Y[8]
        self.B[7] = self.Y[7]
        self.B[6] = self.Y[6]
        self.B[12] = self.Y[5]
        self.B[11] = self.Y[4]

        self.Y[4] = temp[1]
        self.Y[5] = temp[5]
        self.Y[6] = temp[6]
        self.Y[7] = temp[12]
        self.Y[8] = temp[13]

            
    def randomize(self):
        run =random.randrange(1,12)
        if run == 1: 
            self.u_swap()
        elif run == 2:  
            self.U_swap() #2
        elif run==3:  
            self.Uw_swap()
        elif run==4:  
            self.l_swap()
        elif run==5:  
            self.L_swap()
        elif run==6:  
            self.Lw_swap()
        elif run==7:  
            self.r_swap() 
        elif run==8:  
            self.R_swap() 
        elif run==9:  
            self.Rw_swap()
        elif run==10: 
            self.b_swap()
        elif run==11: 
            self.B_swap() 
        else: 
            self.Bw_swap()  
            