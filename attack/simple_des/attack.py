from des import *
import random

#S-BOXES are well-known
s1=[[5,2,1,6,3,4,7,0],[1,4,6,2,0,7,5,3]]
s2=[[4,0,6,5,7,1,3,2],[5,3,0,7,6,2,1,4]]


def reverse_key(k):
  for i1 in range(0):
    k=[k[(i+1)%9] for i in range(9)]
  return k

expansion = lambda R: R[0:2]+[R[3],R[2],R[3],R[2]]+R[4:]
to_bin = lambda x: '0'*(3-len(bin(x).split('b')[1]))+bin(x).split('b')[1]
to_4bin = lambda x: '0'*(4-len(bin(x).split('b')[1]))+bin(x).split('b')[1]



if __name__=='__main__':
  dx_set, sx_set = {x for x in range(16)},{x for x in range(16)}
  
  R = [random.randint(0,1) for i in range(6)]

  while True: 
     
    dx_key, sx_key = [], []
    L1 = [random.randint(0,1) for i in range(6)]
    L1_st = [random.randint(0,1) for i in range(6)]
    pl1, pl1_st = L1+R, L1_st+R
    #plp = [pl1[i] ^ pl1_st[i] for i in range(12)]
    
    EL4, EL4_st = expansion(DES(L1+R)[:6]), expansion(DES(L1_st+R)[:6])
    C1,C1_st=DES(pl1),DES(pl1_st)
    '''
    considero differenza Z2 fra L1, L1_st
    
    in out dallo xor con la chiave ho (all'ultimo round)
    E(L4') = E(L4) ^ E(L4_st) 

    lo confronto con questo output(sotto) e costruisco i sacchettini
    
    R4' ^ L1'  
    
    '''   
    R4_p = [c[0] ^ c[1] for c in zip(C1[len(C1)//2:],C1_st[len(C1_st)//2:])]
    L1_p = [c[0] ^ c[1] for c in zip(pl1[:len(pl1)//2],pl1_st[:len(pl1_st)//2])]
    L1R4 = [c[0] ^ c[1] for c in list(zip(R4_p,L1_p))]
    EL4 = expansion(C1[:len(C1)//2])
    EL4_st = expansion(C1_st[:len(C1_st)//2])
    
    EL4_p = [c[0] ^ c[1] for c in zip(EL4,EL4_st)]  
    sx_o, dx_o = int(''.join([str(c) for c in L1R4[:len(L1R4)//2]]),2),int(''.join([str(c) for c in L1R4[len(L1R4)//2:]]),2)
    sx_p, dx_p = int(''.join([str(c) for c in EL4_p[:len(EL4_p)//2]]),2), int(''.join([str(c) for c in EL4_p[len(EL4_p)//2:]]),2)
    
    for C in range(16):
      for D in range(16):
        if C ^ D == sx_p:
          i1,i2 = int(to_4bin(C)[0]),int(''.join(to_4bin(C)[1:]),2)
          i3,i4 = int(to_4bin(D)[0]),int(''.join(to_4bin(D)[1:]),2)          
          if s1[i1][i2]^s2[i3][i4] == sx_o:
            sx_l4 = int(''.join([str(c) for c in EL4[:len(EL4)//2]]),2)
            sx_l4st = int(''.join([str(c) for c in EL4_st[:len(EL4_st)//2]]),2)
            sx_key+=[C^sx_l4]

    for C in range(16):
      for D in range(16):
        if C ^ D == dx_p:
          i1,i2 = int(to_4bin(C)[0]),int(''.join(to_4bin(C)[1:]),2)
          i3,i4 = int(to_4bin(D)[0]),int(''.join(to_4bin(D)[1:]),2)          
          if s1[i1][i2]^s2[i3][i4] == dx_o:
            dx_l4 = int(''.join([str(c) for c in EL4[len(EL4)//2:]]),2)
            dx_l4st = int(''.join([str(c) for c in EL4_st[len(EL4_st)//2:]]),2)
            dx_key+=[C^dx_l4]
    
    
    print(dx_key)
    print(sx_key)
    
    dx_set = dx_set.intersection(set(dx_key.copy())) 
    sx_set = sx_set.intersection(set(sx_key.copy()))
   
    print('dx set = {}'.format(dx_set))
    print('sx set = {}'.format(sx_set))
    
    if len(dx_set)==0:
      print('ERROR DX')
      exit(1)
    
    if len(sx_set)==0:
      print('ERROR SX')
      exit(1)
      

    if len(dx_set) == 1 and len(sx_set)==1:
      break

        
print('SOL k4 = {}{}'.format(to_4bin(sx_set.pop()),to_4bin(dx_set.pop())))
