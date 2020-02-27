#include<stdio.h>
#include<stdlib.h>
#include<math.h>

long long* fermatFact(unsigned long long n){
  unsigned long long a;
  a = (unsigned long long) sqrt(n);
  long long diff = n-a*a,b,*sol=malloc(sizeof(unsigned long long[2]));
  b = (long long)sqrt((double)(diff));
  printf("\na = %llu diff= %ld\n",a,diff);
  
  while(b*b != diff){
    a+=1;
    printf("\na = %llu b= %ld \n",a,b);
    //printf("\na = %llu\n",a);
    diff = (n-(a*a) <0) ? n-a*a : a*a-n ;
    printf("\n diff = %ld \n",diff);
    b=(long long)sqrt(diff);
  }
  
  sol[0]=a; sol[1]=b;
  return sol;
}


int main(){
  unsigned long long n,*sol;
  printf("\n Inserti N: ");
  scanf("%llu",&n);
  sol = fermatFact(n);
  printf("\nfactors of N = %llu: (%llu, %llu) \n", n, sol[0],sol[1]);
    


  return 0;
}
