import numpy as np
from scipy.io import wavfile
from matplotlib import pyplot as plt
import COLORS  # coloring the output  #

# read the wave file, returns the sample rate and the signal as a NumPy array. #
sample_rate, signal = wavfile.read('voice.wav')

plt.title('Original Signal')
plt.plot(signal)
plt.show()
signal.shape


#
# arg-1 : `sig` the audio signal to be framed
# arg-2 : `fs`  the sampling frequency of the audio signal (default value is 16000 Hz)
# arg-3 : `win_len` the length of each frame in seconds (default value is 0.025s or 25ms)
# arg-4 : `win_hop` the hop size between adjacent frames in seconds (default value is 0.01s or 10ms)
#
def framing(sig, fs=16000, win_len=0.025, win_hop=0.01):
    Frames = []
    # calc the length of each frame and the No. samples to skip between frames
    # based on the sampling frequency
    frame_length = int(win_len * fs)
    frame_step = int(win_hop * fs)
    signal_length = len(sig)
    # calc the amount of overlap between frames #
    frames_overlap = int(frame_length - frame_step)

    # print frame length #
    print("\n" + COLORS.BOLD_RED + "frame length = " +
          COLORS.BOLD_PURPLE + str(frame_length) + "\n"
          + COLORS.RESET_COLOR)

    # iterates over the audio signal #
    for i in range(0, signal_length - frame_length, frame_length):
        if i != 0:
            # if not the 1st frame, add a number of samples to the beginning of the current frame
            # to overlap with the end of the previous frame.
            Frames.append(signal[i - frames_overlap:(i - frames_overlap) + frame_length])
        else:
            # Otherwise, starts the frame at the current position.
            Frames.append(signal[i:i + frame_length])

    # returns the frames as a NumPy array #
    return np.array(Frames)


frames = framing(signal)
print(COLORS.BOLD_CYAN + "Matrix containing frames (one frame per row): \n" + COLORS.BOLD_GREEN)
print(frames)
print(COLORS.RESET_COLOR)

frames.shape
frames = frames.reshape(frames.shape[0] * frames.shape[1], 2)
plt.title('Framed Signal')
plt.plot(frames)
plt.show()
