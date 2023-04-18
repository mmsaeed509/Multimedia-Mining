#!/bin/bash

#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

# Create an empty coding_scp.txt file
> coding_scp.txt

# Loop through the file paths and append them to coding_scp.txt #
for i in {0..9}; do

    for j in {1..20}; do

        # Add leading zero to j counter if less than 10 #
        if [[ "$j" -lt 10 ]]; then

            echo "/home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/wav/${i}_0${j}.wav /home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_0${j}.mfc" >> coding_scp.txt

        else

            echo "/home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/wav/${i}_${j}.wav /home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_${j}.mfc" >> coding_scp.txt

        fi

    done

done
