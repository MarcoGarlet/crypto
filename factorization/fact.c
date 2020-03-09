#include<stdio.h>
#include<stdlib.h>
#include<math.h>

unsigned long long euclid(unsigned long long a, unsigned long long b){
  unsigned long long c;
  if(b>a){
    c=a;
    a=b;
    b=c;
  }
  while(a%b > 0){
    c=a%b;
    a=b;
    b=c;   
  }
  return b;	  
}


long long* fermatFact(unsigned long long n){
  unsigned long long a;
  a = (unsigned long long) sqrt(n);
  long long diff = n-a*a,b,*sol=malloc(sizeof(unsigned long long[2]));
  b = (long long)sqrt((double)(diff));
  while(b*b != diff){
    a+=1;
    diff = (n-(a*a) <0) ? n-a*a : a*a-n ;
    b=(long long)sqrt(diff);
  }
  
  sol[0]=a; sol[1]=b;
  return sol;
}

unsigned long long pollardFact(unsigned long long n){
  // we choose g(x) = x^2+1
  unsigned long long x=2,y=2,d=1,c;
  while(d==1){
    x = ((unsigned long long)pow(x,2)+1)%n;
    y = (unsigned long long)(pow(((unsigned long long)pow(y,2)+1)%n,2)+1)%n;
    c = (y>x)?y-x:x-y; 
    d = euclid(c,n); 
  }
  return d;
}
int main(){
  unsigned long long n,*sol,sol1;
  printf("\n Inserti N: ");
  scanf("%llu",&n);
  sol = fermatFact(n);
  sol1 = pollardFact(n);
  printf("\n[FERMAT] factors of N = %llu: (%llu, %llu) \n", n, sol[0],sol[1]);
  printf("\n[POLLARD] factor of N = %llu: %llu \n", n, sol1);
  return 0;
}
