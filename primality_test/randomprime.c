#include <stdio.h>
#include <stdlib.h>
#include "primality_test.h"
//#include <time.h>
#include <sys/time.h>

int main(int argc, char **argv){
  init_seed();
  double p=(double)1/4; 
  unsigned long long f=0,n,tr=1, lb, ch, precision;
  printf("\n Give me number of bit [1-16]: ");
  scanf("%llu",&n);
  printf("\n Give me precision: ");
  scanf("%llu",&precision);
  
  while((1-p)*100 < precision){
    tr+=1;
    p*=p;
    printf("\n Precision: %lf\n",(1-p)*100);
    
  }
  printf("\n Number of positive tries : %llu, precision: %lf\n",tr,(1-p)*100);
 
  
  lb = pow(2,n);

  ch = rand()%((lb*2))+lb;
  if (ch % 2 ==0 ) ch+=1;
  while(!miller_rabin_probabilistico(ch,tr)){ 
   
    ch = rand()%((lb*2))+lb;
    if (ch%2==0)
      ch+=1;
    //printf("\n choosen %llu \n", ch);
  }
 
  printf("\n MY CHOICE: %u \n", ch);   
  return 0;
}
