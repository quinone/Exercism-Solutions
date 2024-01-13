#include "pangram.h"

char alphabet[]="abcdefghijklmnopqrstuvwxyz";

bool is_pangram(const char *sentence){
    if (sentence != NULL && strlen(sentence) >= strlen(alphabet)){
        size_t different_letter_total = 0;
        //loop  through alphabet
        for (size_t letter=0; letter < strlen(alphabet); letter++){
            // loop through sentence
            for (size_t position=0; position < strlen(sentence); position++){
                if (alphabet[letter] == tolower(sentence[position])){
                    different_letter_total++;
                    break;
                }
            } 
        }
        if (different_letter_total == strlen(alphabet))
            return true;
    }
    return false;
}