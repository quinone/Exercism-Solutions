#include "roman_numerals.h"
#include <string.h>
#include <stdlib.h>


char *to_roman_numeral(unsigned int number){
    char* result = malloc(20);
    int running_total = number;

    if (running_total==1)
        strcpy(result, "I");
    
    return result;
}