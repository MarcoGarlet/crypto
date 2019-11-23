from functools import reduce
import itertools


def gf_degree(a) :
  res = 0
  a >>= 1
  while (a != 0) :
    a >>= 1;
    res += 1;
  return res

def gf_invert(a, mod=0x1B) :
  if a==0: return 0
  v = mod
  g1 = 1
  g2 = 0
  j = gf_degree(a) - 8

  while (a != 1) :
    if (j < 0) :
      a, v = v, a
      g1, g2 = g2, g1
      j = -j

    a ^= v << j
    g1 ^= g2 << j

    a %= 256  
    g1 %= 256 

    j = gf_degree(a) - gf_degree(v)

  return g1

rshift = lambda x,y: [x[(i-y*1)%8] for i in range(8)]
int2vect = lambda c: [int(bit) for bit in bin(c%16).split('b')[1][::-1]+('0'*(4-len(bin(c%16).split('b')[1])))+bin(c//16%16).split('b')[1][::-1]+('0'*(4-len(bin(c//16%16).split('b')[1])))] 
vect2int = lambda v: int(''.join([str(i) for i in v])[::-1],2)
 

cvector = int2vect(0x63)
cmatrix = [[1,0,0,0,1,1,1,1]]+[rshift([1,0,0,0,1,1,1,1],i) for i in range(1,8)]

def sbox_v(xy): return vect2int(list(map(lambda x,y:x^y,[reduce(lambda x,y:x^y, l) for l in [list(map(lambda x,y: x*y, int2vect(gf_invert(xy)), crow)) for crow in cmatrix]],cvector)))

to4matrix = lambda x: [[ord(c) for c in x[i*4:i*4+4]] for i in range(4)]

def decimal2bin(n,t):
  b = []
  while n>0:
    b+=[n%2]
    n=n//2
  while len(b)<t: b+=[0]
  return b[::-1]

passwd = input('Insert secret key [len <= 16]: ')

while len(passwd)>16: passwd = input('Insert secret key [len <= 16]: ')
while len(passwd)<16: passwd+='\x00'

key = to4matrix(passwd)

whitening = lambda key,plaintext: [[ key[i1][i] ^ plaintext[i1][i] for i1 in range(4)] for i in range(4)]


def expand_key(key):
  # NK = 4 in 128 bit
  # see https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf
  pass  

def add_round_key():
  pass
def round(pl):
  pass


if __name__=='__main__':
  plaintext = input('insert plaintext (16 char): ')
  while len(plaintext) != 16: plaintext = input('insert plaintext (16 char): ')
  plaintext = to4matrix(plaintext)
  plaintext_w = whitening(plaintext, key)
  for round in range(10):
    #
    print(round)
    

