from functools import reduce

r = []

def remainders(f):
  cnt = 0
  def wrp(a,b):
    global r
    nonlocal cnt
    if cnt!=0: r+=[a]
    cnt+=1
    return f(a,b)  
  return wrp

@remainders
def euclid(a,b):
  if b>a: a,b=max([a,b]),min([a,b]) 
  if a%b>0: return euclid(b,a%b)
  else: return b 



if __name__ == '__main__':
  a,b = int(input('a: ')), int(input('b: '))
  gcd = euclid(a,b)
  assert (reduce(lambda x,y: x and y, [ri%gcd==0 for ri in r]) == True)	
  print('gcd = {}'.format(gcd))
  



