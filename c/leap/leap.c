#include "leap.h"

bool leap_year(int year){
    if ( year % 100 == 0){
        if (year % 400 != 0){
            return 0;
        }     
        return 1;
    }   
    if (year % 4 == 0)
        return 1;
    return 0;
}

