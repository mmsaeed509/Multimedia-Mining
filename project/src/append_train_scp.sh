#!/bin/bash

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

# Create an empty train_scp.txt file
> ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/train_scp.txt

# Loop through the file paths and append them to train_scp.txt #
for i in {0..9}; do

    for j in {1..20}; do

        # Add leading zero to j counter if less than 10 #
        if [[ "$j" -lt 10 ]]; then

            echo "/home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_0${j}.mfc" >> ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/train_scp.txt

        else

            echo "/home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_${j}.mfc" >> ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/train_scp.txt

        fi

    done

done
