from functools import *
import itertools

lshift = lambda s: [s[(i+1)%len(s)] for i in range(len(s))]
bin2decimal = lambda v: reduce(lambda x,y: x+y, [v[len(v)-1-i]*(2**i) for i in range(len(v)-1,-1,-1)])

def decimal2bin(n,t):
  b = []
  while n>0:
    b+=[n%2]
    n=n//2
  while len(b)<t: b+=[0]
  return b[::-1]

# logs

sep = '\n'+'#'*52+'\n'


# S-Boxes

S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

# Permutation tables

initial_ord = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]

expansion_ord = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

final_ord = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

sbox_perm = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

#Keygen tables

perm_table = [[57,49,41,33,25,17,9,1],[58,50,42,34,26,18,10,2],[59,51,43,35,27,19,11,3],[60,52,44,36,63,55,47,39],[31,23,15,7,62,54,46,38],[30,22,14,6,61,53,45,37],[29,21,13,5,28,20,12,4]]

lefts_table = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

key_comp_table = [[14,17,11,24,1,5,3,28],[15,6,21,10,23,19,12,4],[26,8,16,7,27,20,13,2],[41,52,31,37,47,55,30,40],[51,45,33,48,44,49,39,56],[34,53,46,42,50,36,29,32]]

# keygen perm table yet remove control bit
key = input('Insert key [8 chars]: ')
while len(key)!=8: key = input('Please insert key [8 chars]: ')

key = reduce(lambda x,y: x+y, [ decimal2bin(ord(c),8) for c in key])

key_init_perm = reduce(lambda x,y: x+y, reduce(lambda x,y: x+y, [[[key[perm_table[i][j]-1] for j in range(8)] for i in range(7)]]))

print('K INIT PERM = {}'.format(key_init_perm))

key_pair = [key_init_perm[:len(key_init_perm)//2],key_init_perm[len(key_init_perm)//2:]]

def get_plaintext(): return [x.strip() for x in open(fname, 'r').readlines()]
def initial_permutation(t): return [t[i-1] for i in initial_ord]
def final_permutation(t): return [t[i-1] for i in final_ord] 

def feistel(r, round):
  def expansion(r):
    return [r[i-1] for i in expansion_ord]
  def key_gen():
    for i in range(lefts_table[round-1]):
      key_pair[0] = lshift(key_pair[0])
      key_pair[1] = lshift(key_pair[1])
    C,D = key_pair[0],key_pair[1] 
    k2comp = C+D
    k_round=reduce(lambda x,y: x+y, [[k2comp[key_comp_table[i][j]-1] for j in range(8)] for i in range(6)])
    return k_round
  def value_from_sbox(b,sbox):
    row, column = bin2decimal([b[0],b[-1]]),bin2decimal(b[1:-1])
    return decimal2bin(sbox[row][column],4)
    

  er = expansion(r)
  print('expansion_r = {}'.format(er))
  k_xor_r = [el[0]^el[1] for el in zip(er,key_gen())]
  print('k_{} xor expansion_r = {}'.format(round,k_xor_r))
  sboxes = [k_xor_r[i*6:(i*6)+6] for i in range(8)]
  
  s_box_comp = value_from_sbox(sboxes[0],S1) + value_from_sbox(sboxes[1],S2) + value_from_sbox(sboxes[2],S3) + value_from_sbox(sboxes[3],S4) + value_from_sbox(sboxes[4],S5)+ value_from_sbox(sboxes[5],S6) + value_from_sbox(sboxes[6],S7)+ value_from_sbox(sboxes[7],S8)
  print('sbox compression = {}'.format(s_box_comp))
  return [s_box_comp[i-1] for i in sbox_perm] 



if __name__=='__main__':
  
  passwd = input('Insert plaintext [length multiple of 8]: ')
  while len(passwd)%8!=0: passwd = input('Insert passwd: ')
  for pl in [passwd[8*i:8*i+8] for i in range(len(passwd)//8)]:
    t = reduce(lambda x,y: x+y, [decimal2bin(ord(c),8) for c in pl])
    t = initial_permutation(t)
    print('initial perm = {}'.format(t))
    for i in range(1,17):
      print(sep)
      print('ROUND {}'.format(i))
      l,r = t[:32],t[32:]
      print('\nr_{} = {} \nl_{} = {} \n'.format(i-1,r,i-1,l))
      l_n = r
      
      fr = feistel(r,i)
      print('\n out feistel = {} \n'.format(fr))
      r_n = [el[0]^el[1] for el in zip(fr,l)]  
      t = l_n+r_n
      print(sep)  
    print(sep) 
    print('FINAL PERMUTATION') 
    print('\nr_16 ={} \nl_16 ={}\n'.format(l_n,r_n))
    t=final_permutation(r_n+l_n)
    print('\nFinal perm = {} \n'.format(t))
    t_ascii = [hex(bin2decimal(t[i*8:i*8+8])) for i in range(8)]
    print(sep+'\n'+sep)

    print('RESULT')
    print('\n{}\n'.format(t_ascii))
    print('\n'+''.join([chr(int(x,16)) for x in t_ascii])+'\n')
    print(sep)
    input('Press [enter] for next password')
     
