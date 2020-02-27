#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#include "primality_test.h"

#define NUMERO_COMPOSTO 0
#define NUMERO_PRIMO    1
#define DEBUG           1


int main(int argc, char *argv[]) {
  

 
    char *mode = argv[1];

    if (!strcmp(mode, "deterministico")) {
        int64 n = (int64) atoi(argv[2]);
        puts(test_deterministico(n) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
 	} else if (!strcmp(mode, "fermat_singola_base")) {
        int64 n = (int64) atoi(argv[2]);
        int64 a = (int64) atoi(argv[3]);
        puts(fermat_singola_base(n, a) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "fermat")) {
        int64 n = (int64) atoi(argv[2]);
        puts(test_fermat(n) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_singola_base")) {
        int64 n = (int64) atoi(argv[2]);
        int64 a = (int64) atoi(argv[3]);
        puts(miller_rabin_singola_base(n, a) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_regolare")) {
        int64 n = (int64) atoi(argv[2]);
        puts(miller_rabin_regolare(n) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_probabilistico")) {
        int64 n = (int64) atoi(argv[2]);
        int64 precisione = (int64) atoi(argv[3]);
        puts(miller_rabin_probabilistico(n, precisione) == NUMERO_PRIMO ? "NUMERO PRIMO" : "NUMERO COMPOSTO");
    } else if (!strcmp(mode, "miller_test_errori")) {
        int64 n = (int64) atoi(argv[2]);
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










