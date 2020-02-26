typedef unsigned short int16;
typedef unsigned long int32;

int test_deterministico(int16 n);
int fermat_singola_base(int16 n, int16 a);
int test_fermat(int16 n);
int miller_rabin_singola_base(int16 a, int16 n);
int miller_rabin_regolare(int16 n);
int miller_rabin_probabilistico(int16 n, int16 precisione);
