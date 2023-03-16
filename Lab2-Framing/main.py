import numpy as np
from scipy.io import wavfile
from scipy.fftpack import dct
from matplotlib import pyplot as plt
import COLORS

sample_rate, signal = wavfile.read('voice.wav')
plt.title('Original Signal')
plt.plot(signal)
plt.show()
signal.shape


def framing(sig, fs=16000, win_len=0.025, win_hop=0.01):
    frames = []
    frame_length = int(win_len * fs)
    frame_step = int(win_hop * fs)
    signal_length = len(sig)
    frames_overlap = int(frame_length - frame_step)
    print(COLORS.BOLD_RED + "frame length = " + COLORS.BOLD_PURPLE + str(frame_length) + "\n" + COLORS.RESET_COLOR)
    for i in range(0, signal_length - frame_length, frame_length):
        if i != 0:
            frames.append(signal[i - frames_overlap:(i - frames_overlap) + frame_length])
        else:
            frames.append(signal[i:i + frame_length])

    return np.array(frames)


frames = framing(signal)
print(frames)

frames.shape
frames = frames.reshape(frames.shape[0] * frames.shape[1], 2)
plt.title('Framed Signal')
plt.plot(frames)
plt.show()
