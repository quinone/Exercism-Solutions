#include "protein_translation.h"
#include <string.h>

proteins_t proteins(const char *const rna){
    proteins_t result;
    result.count = 0;
    result.valid = true;
    
    size_t length = strlen(rna);
    if (length == 0) return result; 
    if (length % 3 != 0) {
        result.valid = false;
        return result;
    }
    protein_t decoded_protein;

    char buffer[4];
    // Read 3 letter buffer
    for (size_t i =0; i < length; i=i+3){
        strncpy(buffer, rna+i, 3);
        if (!strcmp(buffer, "AUG")) decoded_protein = 0;
        if (!strcmp(buffer, "UUU")) decoded_protein = 1;
        if (!strcmp(buffer, "UUC")) decoded_protein = 1;
        if (!strcmp(buffer, "UUA")) decoded_protein = 2;
        if (!strcmp(buffer, "UUG")) decoded_protein = 2;
        //if (strcmp(buffer, ''))
    }

    
    // Select protein and increment by 1
    result.proteins[result.count++] = decoded_protein;

    return result;
}
