import itertools
from functools import reduce
import numpy as np
import colorama
from colorama import Fore, Style


class Log:
  def __init__(self):
    self.l = ''
  def info(self,s):
    self.l+='\n\n'+s
  


def pretty_skull(success):
  f1,f2 = 'KEY CRACKED'.split() if success else 'ATTACK FAILED'.split()
  col = Fore.GREEN if success else Fore.RED 
  return Fore.WHITE+'''          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX\''''+col+'''{}'''.format('  '+f1+(' '*(10-(len(f1)+2))))+Fore.WHITE+'''`98v8P\''''+col+'''{}'''.format('  '+f2+(' '*(10-(len(f2)+2))))+Fore.WHITE+'''`XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
'''
  

log=Log()
m, n = 3,3 # n for public, m for private
d = 3
p = ['1101000','1011000','0111000','1100010','1010100','0110100','1010010','1001010','0010110','0001110','1100000','1000010','0011000','0001100','0000110','0000100','1000000','0010000','0000001'] # last digit is constant in polynomial (Z_2)
#p = ['1110000','1101000','1011000','0111000','1100010','1010100','0110100','1010010','1001010','0010110','0001110','1100000','1000010','0011000','0001100','0000110','0000100','1000000','0010000','0000001']
I = []
I_len = 2
private_k = '101' # key to guess


transpose = lambda x: [[x[i][j] for i in range(len(x))] for j in range(len(x[0]))]
complement = lambda x: reduce(lambda x,y: x+y, ['1' if c == '0' else '0' for c in x])
Z2_transform  = lambda x: [int(c%2) for c in x]


def crypt(pub):
  k = pub+private_k # private key
  return reduce(lambda x,y: x^y, [1 for x in [[-1 if (int(k[i]) == 0 and int(t[i]) == 1) else min(int(k[i]),int(t[i])) for i in range(len(p[0])-1)] for t in p] if (-1 not in x and 1 in x)]+[1 for t in p if t[-1]=='1'])
  
'''
After dividing polynomials by t_I test linearity of obtained psi?
'''
def get_psi_remainder(I):
  q = p.copy()
  psi = {}
  for ti in I:
    pos_ti = [i for i in range(len(ti)) if int(ti[i])==1]
    q_p = q.copy()
    q= [m for m in q if not reduce(lambda x,y: x and y,[int(m[i])==1 for i in pos_ti])==True]
    q_diff = set(q_p).difference(set(q))
    psi_t = []
    for term in q_diff: 
      psi_t+=[str(reduce(lambda x,y:x+y, [str(int(term[i])-int(ti[i])) for i in range(len(ti))]))] if term != ti else ['0'*(n+m)+'1']      
    psi[ti]=psi_t
  return q,psi
    
     
 

def offline_phase():
  global I
  I = ['0'*(m-len(x))+x+'0'*(n+1) for x in  [bin(2**index[0]+2**index[1]).split('b')[1] for index in list(itertools.combinations(list(range(d)),I_len))]][::-1]
  #print(I)
  q,psi = get_psi_remainder(I)  
  #print('Q = {}\n\nPSI = {}\n'.format(q,psi))
  return q,psi
     


'''
Applying concept of (d-1)-dimensional cube
'''
    
def online_phase(psi):
  cube_v = ['0'*(d-len(bin(x).split('b')[1]))+bin(x).split('b')[1] for x in range(2**d)]
  system_eq = {}
 
  for k in psi.keys():
    psi_v = [reduce(lambda x,y:x ^ y,[int(psi[k][x][y]) for x in range(len(psi[k]))]) for y in range(len(psi[k][0]))][n:]
    log.info('For term {}'.format(k))
    log.info('\tSuperpolys = {}'.format(psi_v))
    ti_index = [i for i in range(n) if int(k[i])==1]
    log.info('\tIndexes sets = {}'.format(ti_index))
    I_signed = set(range(d)).difference(set(ti_index))
    log.info('\tComplement Indexes sets = {}'.format(I_signed))
    corners = [v for v in cube_v if all([v[x]=='0' for x in I_signed])]
    log.info('\tCorners of cube = {}'.format(corners))

    '''
    If master polynomial is tweaked with cube index {1,2} while keeping 􏰈0, the four 0/1 values of the derived polynomials are obtained. 
    Summation of these four values simply gives the right hand side of the expression.
    The process is repeated in the same way for the next two cube indexes 1,3 and 2,3 
    '''
    system_eq[reduce(lambda x,y: x+y, [str(c) for c in psi_v])]=reduce(lambda x,y: x^y, [crypt(c) for c in corners])

  right_hand = [sum(x) for x in transpose([[-int(x[-1]) for x in system_eq.keys()],[system_eq[x] for x in system_eq.keys()]])]
  return [[int(d) for d in x[:-1]] for x in system_eq.keys()], right_hand  

if __name__=="__main__":
  log.info('### OFFLINE PHASE ###\n') 
  q,psi = offline_phase()
  log.info('q = {}\npsi={}'.format(q,psi)) 
  I_sign = m - I_len; # public value len - I_len
  '''
  psi the key are Ti while values are list of list indicating PSI term
  '''
  log.info('\n### ONLINE PHASE ###\n') 
  var, coeff = online_phase(psi)
  log.info('variable system = {}\ncoeff vector = {}'.format(var,coeff))
  final_res = np.linalg.solve(np.array(var), np.array(coeff))
  cracked_key = reduce(lambda x,y: x+y,[str(x) for x in Z2_transform(final_res)])
  print('key to guess\t=\t'+Fore.RED+'{} '.format(private_k)+Fore.RESET+'\ncracked key\t=\t'+Fore.GREEN+'{} '.format(cracked_key))
  print(pretty_skull(cracked_key==private_k))
  if(cracked_key!=private_k): print(Fore.RED+'{}'.format(log.l))



