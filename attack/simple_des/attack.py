from des import *
import random
import colorama
from colorama import Fore, Style

#S-BOXES are well-known
s1=[[5,2,1,6,3,4,7,0],[1,4,6,2,0,7,5,3]]
s2=[[4,0,6,5,7,1,3,2],[5,3,0,7,6,2,1,4]]


def reverse_key(k):
  for i1 in range(2):
    k=[k[(i-1)%9] for i in range(9)]
  return k

expansion = lambda R: R[0:2]+[R[3],R[2],R[3],R[2]]+R[4:]
to_bin = lambda x: '0'*(3-len(bin(x).split('b')[1]))+bin(x).split('b')[1]
to_4bin = lambda x: '0'*(4-len(bin(x).split('b')[1]))+bin(x).split('b')[1]



if __name__=='__main__':
  dx_set, sx_set = {x for x in range(16)},{x for x in range(16)}
  
  
  #L1 = [0,0,0,1,1,1]
  #L1_st = [1,0,1,1,1,0]
  
  while True: 
    R = [random.randint(0,1) for i in range(6)]   
    dx_key, sx_key = [], []
    L1_st = [random.randint(0,1) for i in range(6)]
    L1 = [random.randint(0,1) for i in range(6)]
    #R = [0,1,1,0,1,1]
    #R = [random.randint(0,1) for i in range(6)]

    pl1, pl1_st = L1+R, L1_st+R
    #plp = [pl1[i] ^ pl1_st[i] for i in range(12)]
    
    C1=DES(pl1)
    
    C1_st = DES(pl1_st)
    print('C1_st = {}'.format(C1_st)) 
    EL4 = expansion(C1[:len(C1)//2])
    EL4_st = expansion(C1_st[:len(C1_st)//2])
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
    print('R4_p = {}, L1_p = {}, L1R4 = {}'.format(R4_p,L1_p,L1R4))
    EL4 = expansion(C1[:len(C1)//2])
    EL4_st = expansion(C1_st[:len(C1_st)//2])
    
    EL4_p = [c[0] ^ c[1] for c in zip(EL4,EL4_st)]    
    print('EL4_p = {}'.format(EL4_p)) 
    sx_o, dx_o = int(''.join([str(c) for c in L1R4[:len(L1R4)//2]]),2),int(''.join([str(c) for c in L1R4[len(L1R4)//2:]]),2)
    sx_p, dx_p = int(''.join([str(c) for c in EL4_p[:len(EL4_p)//2]]),2), int(''.join([str(c) for c in EL4_p[len(EL4_p)//2:]]),2)
    print('sxp = {}'.format(bin(sx_p))) 
    print('sxo = {}'.format(bin(sx_o)))
    for C in range(16):
      for D in range(16):
        if C ^ D == sx_p:
          print('SX C = {}, D = {}'.format(to_4bin(C),to_4bin(D)))
          i1,i2 = int(to_4bin(C)[0]),int(''.join(to_4bin(C)[1:]),2)
          i3,i4 = int(to_4bin(D)[0]),int(''.join(to_4bin(D)[1:]),2)          
          print('C^D = {}'.format(bin(C^D)))
          print('i1 = {}, i2 = {}\n i3 = {}, i4 = {}'.format(bin(i1),bin(i2),bin(i3),bin(i4)))
          print('s1[i1][i2]={},s2[i3][i4] = {}'.format(bin(s1[i1][i2]),bin(s1[i3][i4]))) 
          if s1[i1][i2]^s1[i3][i4] == sx_o:
            print('{}'.format(bin(sx_o)))
            print('s1 = {}, s2 = {}'.format(s1[i1][i2],s2[i3][i4]))
            sx_l4 = int(''.join([str(c) for c in EL4[:len(EL4)//2]]),2)
            print('sx_l4 = {}'.format(bin(sx_l4)))
           
            sx_l4st = int(''.join([str(c) for c in EL4_st[:len(EL4_st)//2]]),2)
            print('sx_l4st = {}\n C^sx_l4 = {} \nD^sx_l4st = {}'.format(bin(sx_l4st),bin(C^sx_l4),bin(D^sx_l4st)))
            

            sx_key+=[C^sx_l4]
        if C ^ D == dx_p:
          print('DX C = {}, D = {}'.format(to_4bin(C),to_4bin(D)))
          i1,i2 = int(to_4bin(C)[0]),int(''.join(to_4bin(C)[1:]),2)
          i3,i4 = int(to_4bin(D)[0]),int(''.join(to_4bin(D)[1:]),2)          
          if s2[i1][i2]^s2[i3][i4] == dx_o:
            print('{}'.format(bin(dx_o)))
            print('s2 = {}, s2 = {}'.format(s2[i1][i2],s2[i3][i4]))

            dx_l4 = int(''.join([str(c) for c in EL4[len(EL4)//2:]]),2)
            dx_l4st = int(''.join([str(c) for c in EL4_st[len(EL4_st)//2:]]),2)
            dx_key+=[C^dx_l4]
 

    print(dx_key)
    print(sx_key)
    
    dx_set = dx_set.intersection(set(dx_key.copy())) 
    sx_set = sx_set.intersection(set(sx_key.copy()))
   
    print('dx set = {}'.format(dx_set))
    print('sx set = {}'.format(sx_set))
    
    if len(dx_set) == 0  or len(sx_set)==0:
      print('ERROR')
      exit(1)
    
    if len(dx_set) == 1 and len(sx_set)==1:
      break

sxk4, dxk4 = to_4bin(sx_set.pop()),to_4bin(dx_set.pop())

k4v1 = (sxk4 +dxk4)
k4v2 = (sxk4 +dxk4)

k4v1 = k4v1[6:]+'1'+k4v1[:6]
k4v2 = k4v2[6:]+'0'+k4v2[:6]

if C1 == DES(pl1,[int(c) for c in k4v1]):
  print('SOL K= '+Fore.GREEN+'{}'.format(k4v1))
else:
  print('SOL K= '+Fore.GREEN+'{}'.format(k4v2))

