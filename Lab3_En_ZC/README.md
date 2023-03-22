Install dependencies
```bash
pip install -r lib.txt
```

to convert `.mp3` to `.wav`

use `ffmpeg` if you use Linux
```bash
ffmpeg -i voice.mp3 voice.wav
```
or use an online tool like [cloudconvert](https://cloudconvert.com/mp3-to-wav)


<u>**Program Requirements:**</u>

Required is a program that divides any input speech signal into frames and computes for each frame its corresponding energy and zero crossing values.

<u>**Inputs:**</u>

- Audio File Path
- Frame size in seconds
- Overlap size in seconds
- Window type to be used 

<u>**Outputs:**</u>

- Vector containing the energy value for each frame. The vector’s length shouldbe equal to the number of frames.
- Vector containing the zero crossing value for each frame. The vector’s length should be equal to the number of frames. 
- A single diagram containing 3 plots:
  - A plot of the framed signal. You can not plot the frames matrix since matrices are 2D and the plot function is used to plot 1D signals. Hence, to make the plot possible, the frames matrix should be used to fill a new vector which will be plotted. The new vector is constructed by concatenating consecutive frames.
  - A plot of the energy vector.
  - A plot of the zero crossing vector
