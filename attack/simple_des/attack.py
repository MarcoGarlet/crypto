from des import *
import random

#S-BOXES are well-known
s1=[[5,2,1,6,3,4,7,0],[1,4,6,2,0,7,5,3]]
s2=[[4,0,6,5,7,1,3,2],[5,3,0,7,6,2,1,4]]

expansion = lambda R: R[0:2]+[R[3],R[2],R[3],R[2]]+R[4:]

if __name__=='__main__':
  R = [random.randint(1) for i in range(6)]
  while True: 
    L1, L1_st = [random.randint(1) for i in range(6)],[random.randint(1) for i in range(6)]
    pl1, pl1_st = R+L1, R+L1_st
    C1, C1_st=DES(pl1),DES(pl1_st)
    '''
    considero differenza Z2 fra L1, L1_st
    
    in out dallo xor con la chiave ho (all'ultimo round)
    E(L4') = E(L4) ^ E(L4_st) 

    lo confronto con questo output(sotto) e costruisco i sacchettini
    
    R4' ^ L1'  
    
    '''    
        


