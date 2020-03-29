import threading
import queue
import itertools
import random
import sys
import math

q=queue.Queue()
r=queue.Queue()
n = int(input('Gimmie n: '))
# Each thread test fact of N with specific EC
curves = list(range(1,n))
random.shuffle(curves)
points = list(itertools.product(range(1,n),range(1,n)))
random.shuffle(points)

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    gcd, x, y = egcd(b % a, a)
    return (gcd, y - (b//a) * x, x)

def randomdecorator(pairs): 
  index=-1
  def rand():
    nonlocal index
    index+=1
    return pairs[index]
  return rand

class Point:
  def __init__(self,pair,b):
    self.x=pair[0]
    self.y=pair[1]
    self.b = b
  def __eq__(self, p):
    return self.x == p.x and self.y == p.y and self.b == p.b
  def __add__(self,p):
    d = (p.x-self.x)%n if p==self else (2*self.y)%n
    num = (p.y-self.y)%n if p==self else (self.x**2+self.b)%n
    if d!=0 and math.gcd(n,d)!=1:
      print('d = {}, n = {}'.format(d,n)) 
      return Point(('Infinity',math.gcd(n,d)),-1)
    invd = egcd(d,n)[1]%n
    m = (num*invd)%n
    # IF NOT EXISTS INVERSE with n then problematic number extend gcd
    return Point(((m**2-self.x-p.x)%n,(m*(self.x-(m**2-self.x))-self.y)%n),self.b)
      
 
randomcurve = randomdecorator(curves)
randompoint =  randomdecorator(points) 

def runner(b): 
  #print("b = {}, c = {}".format(b,c))
  exit = 0
  while exit==0:
    p = Point(randompoint(),b)
    # we impose EC with p(x,y) passing throught my EC with parameter b by computing c
    # y^2 = x^3+bx+c
    # c = y^2-x^3-bx
    c = (p.y**2-p.x**3-b*p.x)%n
    s = p
    while True:
      s += p
      if s.x == 'Infinity':
        if s.y != 1: 
          print("FOUND {}".format(s.y))
          r.put(s.y)
        exit = 1
        break
  q.task_done()    
      
if __name__=="__main__":
  for i in range(90):
    b = randomcurve()
    q.put(b)
    print("Thread number: {}\r".format(i))
    t=threading.Thread(target=runner(b))        
    t.start()
q.join()
print(r.get())


