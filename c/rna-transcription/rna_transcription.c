#include "rna_transcription.h"

char *to_rna(const char *dna)
{
    size_t length = strlen(dna);
    char *rna = malloc(length + 1);
    for (size_t n = 0; n < length; n++){
        switch (dna[n])
        {
           
        case 'G':
            rna[n]='C';
            break;
        case 'C':
            rna[n]='G';
            break;
        case 'T':
            rna[n]='A';
            break;
        case 'A':
            rna[n]='U';
            break;
        default:
            break;
        }
    }
    // Add null-terminate to rna
    rna[length] = '\0';
    return rna;
}
