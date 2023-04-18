#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################

Set-Content -Path ./trans.mlf -Value '#!MLF!#'

$output = for ($i=0; $i -le 9; $i++) {

    for ($j=1; $j -le 20; $j++) {

        $fileName = "*/${i}_$('{0:d2}' -f $j).lab"
        Write-Output "`"$fileName`""
        Write-Output "SIL"

        switch ($i) {

            0 { Write-Output "ZERO" }
            1 { Write-Output "ONE" }
            2 { Write-Output "TWO" }
            3 { Write-Output "THREE" }
            4 { Write-Output "FOUR" }
            5 { Write-Output "FIVE" }
            6 { Write-Output "SIX" }
            7 { Write-Output "SEVEN" }
            8 { Write-Output "EIGHT" }
            9 { Write-Output "NINE" }

        }
        Write-Output "SIL"
        Write-Output "."

    }
    
}

$output | Out-File -FilePath ./trans.mlf -Append
