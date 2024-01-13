#include "isogram.h"


bool is_isogram(const char phrase[]) {

    // check if null
    if (phrase != NULL){
        
        int length = strlen(phrase); //get length of phras
        
        // check for empty phrase
        if (length == 0){
        return true;
        }
        
        for (int left = 0; left<=length-2; left++){
            // Skip outter loop if - or space
            if (phrase[left] == '-' || phrase[left] == ' ')
                continue;

            for (int next = left + 1; next <= length-1; next++){
                // Skip inner loop if - or space
                if(phrase[next]== '-')
                    continue;

                if (tolower(phrase[left]) == tolower(phrase[next]))
                    return false;
            }
        }
        return true;    
    }
    return false;
    
}
        /*
    int i = 0;
    while(phrase[i+1] != '\0'){
        int j = i + 1;
        while(phrase[j] != '\0'){
            if (phrase[i] == phrase[j])
                return false;
        }
        i++;
    }
return true;
}*/
/*    
    for (int i = 0; phrase[i+1] != '\0'; i++){
        if (phrase[i] == ' ' || phrase[i] == '-')
            continue;
        for (int j = i+1; phrase[j] != '\0'; j++){
            if (phrase[j] == ' ' || phrase[j] == '-')
                continue;
            if (phrase[i] == phrase[j])
                return false;
        }
    }
    return true;
*/   
/*
    size_t len = sizeof(phrase)/sizeof(phrase[0]);
    for (size_t i = 0; i < len-1; i++)
        for (size_t j = i+1; j < len; j++){
            if (phrase[j] == phrase[i])
                return false;
        }
    return true;
}*/
