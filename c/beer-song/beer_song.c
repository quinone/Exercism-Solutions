#include "beer_song.h"
#include <stdlib.h>
#include <stdio.h>

void recite(uint8_t start_bottles, uint8_t take_down, char **song);

char *song[] = {
    /*index[0]*/
    "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n",
    /*index[1]*/
    " bottle of beer on the wall, ",
    /*index[2]*/
    " bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n",
    /*index[3]*/
    " bottles of beer on the wall, ",
    /*index[4]*/
    " bottles of beer.\nTake one down and pass it around, ",
    /*index[5]*/
    " bottle of beer on the wall.\n",
    /*index[6]*/
    " bottles of beer on the wall, ",
    /*index[7]*/
    " bottles of beer.\nTake one down and pass it around, ",
    /*index[8]*/
    " bottles of beer on the wall.\n"
    };

void recite(uint8_t start_bottles, uint8_t take_down, char **song)
{
    

}

    /*
    uint8_t counter = 0;
    if (!(counter == take_down))
    {
        if(start_bottles == 0){
            printf("%s",song[0]);  
        }
        else if(start_bottles == 1){
            printf("%u%s%u%s",
                   start_bottles,
                   song[1],
                   start_bottles,
                   song[2]);
            counter++;
            recite(start_bottles-1, take_down, song);
        }
        else if(start_bottles == 2){
            printf("%u%s%u%s%u%s",
                   start_bottles,
                   song[3],
                   start_bottles,
                   song[4],
                   start_bottles-1,
                   song[5]);
            counter++;
            recite(start_bottles-1, take_down, song);
        }
        else if (start_bottles > 2){
            printf("%u%s%u%s%u%s",
                   start_bottles,
                   song[6],
                   start_bottles,
                   song[7],
                   start_bottles-1,
                   song[8]);
            counter++;
            recite(start_bottles-1, take_down, song);
        }
    }
}

*/