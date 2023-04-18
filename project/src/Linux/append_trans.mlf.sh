#!/bin/bash

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

echo '#!MLF!#' > trans.mlf

for i in $(seq -f "%01g" 0 9); do

    for j in $(seq -f "%02g" 1 20); do

        echo "\"*/${i}_${j}.lab\""
        echo "SIL"

        case $i in

            0) echo "ZERO" ;;
            1) echo "ONE" ;;
            2) echo "TWO" ;;
            3) echo "THREE" ;;
            4) echo "FOUR" ;;
            5) echo "FIVE" ;;
            6) echo "SIX" ;;
            7) echo "SEVEN" ;;
            8) echo "EIGHT" ;;
            9) echo "NINE" ;;

        esac
        echo "SIL"
        echo "."

    done
    
done >> trans.mlf
