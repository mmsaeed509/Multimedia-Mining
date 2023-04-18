#!/bin/bash

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

# needed Paths #
PATH=$(pwd)
MFCC_PATH="${PATH}/mfcc"

# Create an empty train_scp.txt file #
> train_scp.txt

# Loop through the file paths and append them to train_scp.txt #
for i in {0..9}; do

    for j in {1..20}; do

        # Add leading zero to j counter if less than 10 #
        if [[ "$j" -lt 10 ]]; then

            echo "${MFCC_PATH}/${i}_0${j}.mfc" >> train_scp.txt

        else

            echo "${MFCC_PATH}/${i}_${j}.mfc" >> train_scp.txt

        fi

    done

done
