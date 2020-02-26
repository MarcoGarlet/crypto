#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>


#include "primality_test.h"

#define NUMERO_COMPOSTO 0
#define NUMERO_PRIMO    1
#define DEBUG           1


int main(int argc, char *argv[]) {
  

    time_t t;
    srand((unsigned) time(&t));
 
    char *mode = argv[1];

    if (!strcmp(mode, "deterministico")) {
        int16 n = (int16) atoi(argv[2]);
        puts(test_deterministico(n) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
 	} else if (!strcmp(mode, "fermat_singola_base")) {
        int16 n = (int16) atoi(argv[2]);
        int16 a = (int16) atoi(argv[3]);
        puts(fermat_singola_base(n, a) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "fermat")) {
        int16 n = (int16) atoi(argv[2]);
        puts(test_fermat(n) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_singola_base")) {
        int16 n = (int16) atoi(argv[2]);
        int16 a = (int16) atoi(argv[3]);
        puts(miller_rabin_singola_base(n, a) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_regolare")) {
        int16 n = (int16) atoi(argv[2]);
        puts(miller_rabin_regolare(n) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_probabilistico")) {
        int16 n = (int16) atoi(argv[2]);
        int16 precisione = (int16) atoi(argv[3]);
        puts(miller_rabin_probabilistico(n, precisione) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_test_errori")) {
        int16 n = (int16) atoi(argv[2]);
        int classe = test_deterministico(n);

        // Scelgo il valore di a
        for (int i = 2; i < (n - 1); i++) {
            if (miller_rabin_singola_base(n,i) != classe) {
                printf("Errore con n = %d e a = %d \n", n, i);
            }
        }
    }

    return 0;
}



int test_deterministico(int16 n){
  int i;
  for (i=2; i <= (int)ceil(sqrt(n)) ; i++){
    if (n % i == 0)
      return 0;
  }
  return 1;
}

int fermat_singola_base(int16 n, int16 a){
  if (a>=n-1)
    printf("\nWarning a must be in [2, n-2] \n");
  return ((unsigned long)pow((double)a,(double)n-1)) % n == 1;
}

int test_fermat(int16 n){
  unsigned long a,i,k = rand()%10+2;
  for (i=0; i<k;i++){
    a = (unsigned long)rand()%(n-3) + 2;
    printf("\n a = %lu \n", a);
    if (fermat_singola_base(n,a)) return 1;
  } 
  return 0;
}


int miller_rabin_singola_base(int16 a, int16 b){
  // a = n, b = a
  unsigned int n=a-1, k=0, q=1;
  int j=0;
  while(n%2 == 0){
    k+=1;
    n/=2;
  }
  q = n;
 
  printf("\n k = %u, q = %u \n", k, q);
  if (b > a-2 || b < 1)
    printf("\n Warning the base selected is out of bound\n");
  if (a%b == 0) return 0;
  if((b*q) % a == 1) return 1;
  for(; j < k+1; j++){
    printf("\n in for =  %u, a-1 = %u\n",((unsigned int)pow(b,(unsigned int)pow(2,j)*q))%a, a-1);

    if (((unsigned int)pow(b,(unsigned int)pow(2,j)*q))%a == a-1)
      return 1;
  } 
  return 0;
}

int miller_rabin_regolare(int16 n){
  unsigned int bases[] = {2,7,61};
  int i;
  for(i=0; i<3 && bases[i] < n-1; i++){
    printf("\n Test bases %u with n = %u\n", bases[i],n);
    if (miller_rabin_singola_base(n,bases[i]) ==1)
      return 1;
  }
  return 0;
}

int miller_rabin_probabilistico(int16 n, int16 p){
  unsigned int i,k;
  for(i=0; i<p; i++){
    k = (rand()%(n-3))+2;  
    printf("\n Choosen base = %u \n", k);
    if(miller_rabin_singola_base(n,k) == 1) 
      return 1;
  }
  return 0;
}










