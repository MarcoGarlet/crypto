import threading
import queue
import itertools
import random
import sys
import math
import os
q=queue.Queue()
r=queue.Queue()
n = int(input('Gimmie n: '))

def b_gen():
  while True:
    yield random.randint(1,n)

def pairs_gen():
  while True:
    yield (random.randint(1,n),random.randint(1,n))

curves = b_gen()
points = pairs_gen()

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    gcd, x, y = egcd(b % a, a)
    return (gcd, y - (b//a) * x, x)

def randomdecorator(pairs): 
  def rand():
    return next(pairs)
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
  
  def __mul__(self, p):
    r = self
    for i in range(p):
      r+=self
      if r.x == 'Infinity': break
    return r
      
 
randomcurve = randomdecorator(curves)
randompoint =  randomdecorator(points) 

def runner(): 
  b = q.get()
  clock_ec,cmax = 0,random.randint(2**int(math.log(n,2)-1),2**int(math.log(n,2)+1))
  pq = randompoint() 
  print(pq)
  p = Point(pq,b)
  c = (p.y**2-p.x**3-b*p.x)%n
  s = p
  k = 2
  while clock_ec < cmax:
    clock_ec+=1
    s = s*k
    if s.x == 'Infinity':
      if s.y != 1: 
        print("FOUND {}".format(s.y))
        r.put(s.y)
      else: print("Invalid EC")
      break
  q.task_done()    
      
if __name__=="__main__":
  for i in range(int(input('How many threads(EC)? '))):
    b = randomcurve()
    q.put(b)
    t = threading.Thread(target=runner)    
    t.start()
  q.join()
  print('Factor of n = {}'.format(r.get()))


