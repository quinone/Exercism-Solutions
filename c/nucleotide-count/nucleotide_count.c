#include "nucleotide_count.h"


char *count(const char *dna_strand)
{
    char *report;
    
    // Initalize nucleotide counts to 0
    int nucleotide[]={0,0,0,0};

    // Loop through dna_strand
    for (; *dna_strand; dna_strand++){
        
        switch (*dna_strand)
        {
        
        case 'A':
            nucleotide[0]++;
            break;
        case 'C':
            nucleotide[1]++;
            break;
        case 'G':
            nucleotide[2]++;
            break;
        case 'T':
            nucleotide[3]++;
            break;
        default:
            if ((report = malloc(1)) == NULL){
                return NULL;
            }
            *report = '\0';
            return report;
        }
    }
    size_t report_size = snprintf(NULL, 0,"A:%d C:%d G:%d T:%d",
        nucleotide[0],
        nucleotide[1],
        nucleotide[2],
        nucleotide[3]);

    report=malloc(report_size + 1);

    snprintf(report, report_size + 1,"A:%d C:%d G:%d T:%d",
        nucleotide[0],
        nucleotide[1],
        nucleotide[2],
        nucleotide[3]);

    return report;

}