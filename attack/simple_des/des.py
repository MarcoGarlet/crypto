import random

#CHOOSEN PLAINTEXT ATTACK

secret_keys = [0,0,1,0,0,1,1,0,1]

s1=[[5,2,1,6,3,4,7,0],[1,4,6,2,0,7,5,3]]
s2=[[4,0,6,5,7,1,3,2],[5,3,0,7,6,2,1,4]]

def r_keys():
  global secret_keys
  while True:
    secret_keys=[secret_keys[(i+1)%9] for i in range(9)]
    yield secret_keys[0:8]

expansion = lambda R: R[0:2]+[R[3],R[2],R[3],R[2]]+R[4:]
to_bin = lambda x: '0'*(3-len(bin(x).split('b')[1]))+bin(x).split('b')[1]
round_keys = r_keys()

def clear_skey():
  global secret_keys 
  secret_keys= [0,0,1,0,0,1,1,0,1]



def F(R):
  R,k = expansion(R), next(round_keys)
  print('R = {}\n k = {}'.format(R,k))
  R = [R[i]^k[i] for i in range(len(R))] 
  C,D = R[:4],R[4:]
  C_comp = s1[C[0]][int(''.join([str(i) for i in C[1:]]),2)]
  D_comp = s2[D[0]][int(''.join([str(i) for i in D[1:]]),2)]
  return [int(c) for c in to_bin(C_comp)]+[int(c) for c in to_bin(D_comp)]


def DES(plaintext):
  clear_skey()
  print('SECRET = {}'.format(secret_keys))
  Li,Ri = plaintext[:len(plaintext)//2],plaintext[len(plaintext)//2:]
  for i in range(3):
    Rn = F(Ri)  
    print(Rn) 
    print(Li)
    Rn = [Rn[i] ^ Li[i] for i in range(len(Li))]
    Li = Ri
    Ri = Rn
    print('Li={}, Ri={} '.format(Li,Ri))
   
  return Li+Ri






    




