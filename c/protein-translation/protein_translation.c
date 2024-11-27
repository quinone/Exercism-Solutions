#include "protein_translation.h"
#include <string.h>

proteins_t proteins(const char *const rna){
    proteins_t result;
    result.count = 0;
    result.valid = true;
    
    size_t length = strlen(rna);
    protein_t decoded_protein;

    char buffer[4];
    // Read 3 letter buffer
    for (size_t i =0; i < length; i=i+3){
        strncpy(buffer, rna+i, 3);
        if ((buffer[0] != 'U')&&(buffer[0] != 'A')) {
            result.valid = false;
            return result;
        }
        if ((buffer[1] == 0) ||(buffer[2]==0)){
            result.valid = false;
            return result;
        }
        if ((!strcmp(buffer, "UAA"))||(!strcmp(buffer, "UAG"))||(!strcmp(buffer, "UGA"))){
            break;
        }

        if (!strcmp(buffer, "AUG")) decoded_protein = 0;
        else if ((!strcmp(buffer, "UUU"))||(!strcmp(buffer, "UUC"))) decoded_protein = 1;
        else if ((!strcmp(buffer, "UUA"))||(!strcmp(buffer, "UUG"))) decoded_protein = 2;
        else if ((!strcmp(buffer, "UCU"))||(!strcmp(buffer, "UCC"))||(!strcmp(buffer, "UCA"))||(!strcmp(buffer, "UCG"))) decoded_protein = 3;
        else if ((!strcmp(buffer, "UAU"))|| (!strcmp(buffer, "UAC"))) decoded_protein = 4; 
        else if ((!strcmp(buffer, "UGU"))||(!strcmp(buffer, "UGC"))) decoded_protein = 5;
        else if (!strcmp(buffer, "UGG")) decoded_protein = 6;
        else {
            result.valid = false;
            return result;
        }
        result.proteins[result.count++] = decoded_protein;  
    }
    return result;
}
