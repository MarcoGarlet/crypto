#include <stdio.h>
#include <stdlib.h>
#include "primality_test.h"

int main(int argc, char **argv){
  time_t t;
  srand((unsigned) time(&t));
 

  unsigned long long f=0,n, p, lb, ch;
  printf("\n Give me number of bit [1-16]: ");
  scanf("%llu",&n);
  printf("\n Give me precision: ");
  scanf("%llu",&p);
  /*
    considering only odd number and test primality for that, first choice would be random and then test number sequentially
  */
  lb = pow(2,n);
  ch = rand()%((lb*2)-lb)+lb;
  if (ch % 2 ==0 ) ch+=1;
  while(!miller_rabin_probabilistico(ch,p)){ 
    //printf("\n bad Coiche: %u \n",ch); 
    ch = rand()%((lb*2)-lb)+lb;
    if (ch%2==0)
      ch+=1;
  }
 
  printf("\n MY CHOICE: %u \n", ch);   
  return 0;
}
