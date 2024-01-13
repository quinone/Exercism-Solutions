#include "luhn.h"
#include <string.h>


bool luhn(const char *num){
    // check if zero
    //if (*num == '0')
    //    return false;

    size_t num_length = strlen(num);
    //check if length of num is more than 2
    if (num_length < 2){
        return false;
    }
      
    size_t temp[num_length];
    // loop to load number into an int[]  
    for (size_t counter = 0; counter < num_length ; counter++){
        if (num[counter] == ' ')
            continue;

        temp[counter] = num[counter] - '0';
    }
    
    // loop through doubling every second from the right
    for (size_t start = num_length - 2; start > 0 ; start = start - 2){   
        size_t digit_doubled = temp[start] * 2;
        if (digit_doubled > 9){
            digit_doubled = digit_doubled - 9;
        }
        temp[start] = digit_doubled;
    }

    // loop to sum numbers
    size_t total = 0;
    
    for (size_t j = 0; j < num_length ; j++){
        total = total + temp[j];
    }

    return (total % 10 == 0);
}