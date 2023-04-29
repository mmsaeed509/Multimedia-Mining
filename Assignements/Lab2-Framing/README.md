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

Required is a program that divides any input speech signal into frames. The user can specify any frame size, any overlap size and any window type.

<u>**Inputs:**</u>

- Audio File Path
- Frame size in seconds
- Overlap size in seconds
- Window type to be used 

<u>**Outputs:**</u>

- Matrix containing frames (one frame per row)
- Plot of 
- Plot of framed signal. This is to ensure that you have framed correctly. If youchoose a certain frame size and an overlap size of 50% of the frame size, the
framed signal’s plot should be almost twice the length of the original signal’s
plot.

> <u>**NOTE:**</u>
> 
> **You can not plot the frames matrix since matrices are 2D and the plot
function is used to plot 1D signals. Hence, to make the plot possible, the
frames matrix should be used to fill a new vector which will be plotted. The
new vector is constructed by concatenating consecutive frames.**

<u>**Program Summary:**</u>

The student uses the `wavread` function to read the audio file into a vector, as well as the sampling rate. Then, the frame size and overlap size (in seconds) can be convertedinto samples. In other words,

- Frame size (samples) = frame size (seconds) * Sampling Rate (samples/second)
- Overlap size (samples) = Overlap size (seconds) * Sampling Rate (samples/second)

Then the student can iterate on the vector containing the data, and extract samples
equivalent to the frame size in samples and with overlap equivalent to overlap size insamples. Such frames are placed in a new matrix, where each row corresponds to a
frame. If the user chose a rectangular window, then the previous matrix is the final
one. Else, if the user chose a hamming or hanning window, then the student shouldconstruct a hamming/hanning window of the same size as the frame size, and multiplyeach row of the frames matrix by this window. The student should then plot the
original and the framed signal.

<u>**Sample code:**</u>

```python
%parameters: frameshift, samplerate, framewidth
shift = round(frameshift * samplerate);
framesize = round(framewidth * samplerate);

nframes = ciel((length(wave) – framesize)/shift );
frames = zeros(nframes,framesize);

for(i=1:nframes)
    frames(i,:) = wave( ((i1)*shift+1):((i1)*shift+framesize) )';
end

```