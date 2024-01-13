#include "roman_numerals.h"

char *to_roman_numeral(unsigned int number){
    unsigned int current_total = number;
    char *string_number = malloc(20);
    bool string_initalized = false;
    if (current_total <= 10){
            return below_ten(current_total); 
    }
    while (true){
        if (current_total>1000){
            if (string_initalized){
                strcat(string_number,"M");
            } else {
                strcpy(string_number, "M");
                string_initalized=true;
            }
            current_total = current_total-1000;
        }
        if (current_total<40 && current_total >19){
            if (string_initalized){
                strcat(string_number,"X");
            } else {
                strcpy(string_number, "X");
                string_initalized=true;
            }
            current_total = current_total-10;
        }
        if (current_total <= 10){
            strcat(string_number, below_ten(current_total));
            break; 
        }         
    }

    return string_number;
}
char *below_ten(unsigned int number){
    // Maximum length for a Roman numeral representation is 4 characters
    char *converted_number = malloc(5);

    switch (number) {
        case 1: strcpy(converted_number, "I"); break;
        case 2: strcpy(converted_number, "II"); break;
        case 3: strcpy(converted_number, "III"); break;
        case 4: strcpy(converted_number, "IV"); break;
        case 5: strcpy(converted_number, "V"); break;
        case 6: strcpy(converted_number, "VI"); break;
        case 7: strcpy(converted_number, "VII"); break;
        case 8: strcpy(converted_number, "VIII"); break;
        case 9: strcpy(converted_number, "IX"); break;
        case 10: strcpy(converted_number, "X"); break;
        default: free(converted_number); return NULL;  // Handle unexpected values
    }

    return converted_number;
}



        