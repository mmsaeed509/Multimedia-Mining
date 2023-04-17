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
> ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/coding_scp.txt

# Loop through the file paths and append them to coding_scp.txt #
for i in {0..9}; do

    for j in {1..20}; do

        # Add leading zero to j counter if less than 10 #
        if [[ "$j" -lt 10 ]]; then

            echo "~/GitHub/FCAI-CU/Multimedia-Mining/project/src/wav/${i}_0${j}.wav ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_0${j}.mfc" >> ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/coding_scp.txt

        else

            echo "~/GitHub/FCAI-CU/Multimedia-Mining/project/src/wav/${i}_0${j}.wav ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_${j}.mfc" >> ~/GitHub/FCAI-CU/Multimedia-Mining/project/src/coding_scp.txt

        fi

    done

done
