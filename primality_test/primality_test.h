#include<math.h>
#include <time.h>

typedef unsigned short int16;
typedef unsigned long int32;
typedef unsigned long long int64;

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

int miller_rabin_singola_base(int64 a, int64 b){
  // a = n, b = a
  int64 n=a-1, k=0, q=1, j;
  while(n%2 == 0){
    k+=1;
    n=(int64)n/2;
  }
  //printf("\n k = %u \n",k);
  q = n;
 
  if (a%b == 0) return 0;
  if(((int64)(pow(b,q))) % a == 1) return 1;
  for(j=0; j < k; j++){
    //printf("\n2 alla %u * %u = %u \n",j,q,(unsigned long)pow(2,j)*q);
    if (((int64)pow(b,((int64)pow(2,j))*q))%a == a-1)
      return 1;
  } 
  return 0;
}

int miller_rabin_regolare(int64 n){
  int64 bases[] = {2,7,61};
  int i;
  for(i=0; i<3 && bases[i] < n-1; i++){
    printf("\n Test bases %u with n = %u\n", bases[i],n);
    if (miller_rabin_singola_base(n,bases[i]) ==1)
      return 1;
  }
  return 0;
}
int miller_rabin_probabilistico(int64 n, int64 p){
  int64 k,i,pr=0, t = p;
  time_t at;

  srand((unsigned) time(&at));
 
  for(i=0; i<t; i++){
    //printf("\n Choosen base = %u \n", k);
    k = rand()%(n-3)+2;
    if(miller_rabin_singola_base(n,k) ==0) 
      return 0;
  }

  return 1;
}

