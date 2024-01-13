#include "reverse_string.h"
#include <string.h>
#include <stdlib.h>

char *reverse(const char *value)
{
    size_t length = strlen(value);
    char *rev = malloc((length+1) * sizeof(char));
    
    for(int i = length-1; *value != '\0'; value++, i-- ){
        rev[i] = *value;
    }

    return rev;
}
