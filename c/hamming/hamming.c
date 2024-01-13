#include "hamming.h"

#include <string.h>

int compute(const char *lhs, const char *rhs)
{    
    int distance = 0;

    //for (int i = 0; i < (int)lhs_length; i++)
    for (; *lhs && *rhs ; lhs++, rhs++)
    {
        if (*lhs != *rhs)
        {
            distance++;
        }
    }

    return (*lhs || *rhs ) ? -1 : distance;
    
}