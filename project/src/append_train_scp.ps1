#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################


# Create an empty train_scp.txt file
New-Item -ItemType File -Path "train_scp.txt" -Force | Out-Null

# Loop through the file paths and append them to train_scp.txt #
for ($i=0; $i -le 9; $i++) {

    for ($j=1; $j -le 20; $j++) {

        # Add leading zero to j counter if less than 10 #
        if ($j -lt 10) {

            Add-Content -Path "train_scp.txt" -Value "/home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_0${j}.mfc"

        } else {

            Add-Content -Path "train_scp.txt" -Value "/home/ozil/GitHub/FCAI-CU/Multimedia-Mining/project/src/mfcc/${i}_${j}.mfc"

        }

    }

}
