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
WAV_PATH="${PATH}/wav"
MFCC_PATH="${PATH}/mfcc"

# Create an empty coding_scp.txt file #
> coding_scp.txt

# Loop through the file paths and append them to coding_scp.txt #
for i in {0..9}; do

    for j in {1..20}; do

        # Add leading zero to j counter if less than 10 #
        if [[ "$j" -lt 10 ]]; then

            echo "${WAV_PATH}/${i}_0${j}.wav ${MFCC_PATH}/${i}_0${j}.mfc" >> coding_scp.txt

        else

            echo "${WAV_PATH}/${i}_${j}.wav ${MFCC_PATH}/${i}_${j}.mfc" >> coding_scp.txt

        fi

    done

done
