from functools import reduce
import itertools

mask1 = mask2 = polyred = None

def setGF2(degree, irPoly):
    def i2P(sInt):
        return [(sInt >> i) & 1
                for i in reversed(range(sInt.bit_length()))]    
    
    global mask1, mask2, polyred
    mask1 = mask2 = 1 << degree
    mask2 -= 1
    polyred = reduce(lambda x, y: (x << 1) + y, i2P(irPoly)[1:])
        
def multGF2(p1, p2):
    p = 0
    while p2:
        if p2 & 1:
            p ^= p1
        p1 <<= 1
        if p1 & mask1:
            p1 ^= polyred
        p2 >>= 1
    return p & mask2

# Define binary field GF(2^8)/x^8 + x^4 + x^3 + x + 1
setGF2(8, 0b100011011)


def gf_degree(a) :
  if a==0: return 0
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

#passwd='\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98'

while len(passwd)>16: passwd = input('Insert secret key [len <= 16]: ')
while len(passwd)<16: passwd+='\x00'

key = to4matrix(passwd)

whitening = lambda key,plaintext: [[ key[i1][i] ^ plaintext[i1][i] for i1 in range(4)] for i in range(4)]

rotword = lambda x: [x[1],x[2],x[-1],x[0]]
subword = lambda x: sbox_v(x)


def expand_key(key):
  # see https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf
  w = [key]
  rcon = 0x1
  for i in range(10):
    print('STAGE {}'.format(i))
    current_w=w[-1]
    wl = current_w[-1]
    #ROTWORD
    rcon_v = [rcon,0,0,0]
    rcon=multGF2(rcon,2)
    
    x=rotword(wl)
    print([hex(el) for el in rcon_v])
    y=[subword(el) for el in x]
    z=[rcon_v[i]^y[i] for i in range(4)]
    print([hex(el) for el in z])
    wn = [current_w[0][i] ^ z[i] for i in range(4)]
    print([hex(el) for el in wn])
    wn1= [wn[i] ^ current_w[1][i] for i in range(4)]
    wn2= [wn1[i] ^ current_w[2][i] for i in range(4)]
    wn3= [wn2[i] ^ current_w[3][i] for i in range(4)]
    w+=[[wn,wn1,wn2,wn3]]
    
    #RCON
  for m in w:
    for l in m:
      for el in l:
        print(hex(el),end=' ')
      print()
    print('--------------------------')
    

expand_key(key)

def add_round_key():
  pass

def sub_bytes():
  pass

def shift_rows():
  pass

def mix_columns():
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
    

