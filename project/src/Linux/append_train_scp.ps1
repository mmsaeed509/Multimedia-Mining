#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

# needed Paths #
$PATH = (Get-Location).Path
$MFCC_PATH = "$PATH\mfcc"

# Create an empty train_scp.txt file #
New-Item -ItemType file "train_scp.txt" -Force

# Loop through the file paths and append them to train_scp.txt #
for ($i=0; $i -lt 10; $i++) {

    for ($j=1; $j -le 20; $j++) {

        # Add leading zero to j counter if less than 10 #
        if ($j -lt 10) {

            Add-Content "train_scp.txt" "$MFCC_PATH\$i`_0$j.mfc"

        } else {

            Add-Content "train_scp.txt" "$MFCC_PATH\$i`_$j.mfc"

        }

    }

}
