#####################################
#                                   #
#  @author      : 00xWolf           #
#    GitHub    : @mmsaeed509       #
#    Developer : Mahmoud Mohamed   #
#  﫥  Copyright : Mahmoud Mohamed   #
#                                   #
#####################################
#
# import numpy as np
# from scipy.io import wavfile
# from matplotlib import pyplot as plt

import COLORS  # coloring the output  #
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt


#
# # read the wave file, returns the sample rate and the signal as a NumPy array. #
# sample_rate, signal = wavfile.read('voice.wav')
#

def read_audio_file(file_path="./voice.wav"):
    # Reads an audio file from the given file path and returns its sample rate and signal data.
    sample_rate, signal = scipy.io.wavfile.read(file_path)
    return sample_rate, signal


#
# #
# # arg-1 : `sig` the audio signal to be framed
# # arg-2 : `fs`  the sampling frequency of the audio signal (default value is 16000 Hz)
# # arg-3 : `win_len` the length of each frame in seconds (default value is 0.025s or 25ms)
# # arg-4 : `win_hop` the hop size between adjacent frames in seconds (default value is 0.01s or 10ms)
# #
# def framing(sig, fs=16000, win_len=5, win_hop=1):
#     Frames = []
#     # calc the length of each frame and the No. samples to skip between frames
#     # based on the sampling frequency
#     frame_length = int(win_len * fs)
#     frame_step = int(win_hop * fs)
#     signal_length = len(sig)
#     # calc the amount of overlap between frames #
#     frames_overlap = int(frame_length - frame_step)
#
#     # print frame length #
#     print("\n" + COLORS.BOLD_RED + "frame length = " +
#           COLORS.BOLD_PURPLE + str(frame_length) + "\n"
#           + COLORS.RESET_COLOR)
#
#     # iterates over the audio signal #
#     for i in range(0, signal_length - frame_length, frame_length):
#         if i != 0:
#             # if not the 1st frame, add a number of samples to the beginning of the current frame
#             # to overlap with the end of the previous frame.
#             Frames.append(signal[i - frames_overlap:(i - frames_overlap) + frame_length])
#         else:
#             # Otherwise, starts the frame at the current position.
#             Frames.append(signal[i:i + frame_length])
#
#     # returns the frames as a NumPy array #
#     return np.array(Frames)
#
#
# frames = framing(signal)
#
# frames.shape
# frames = frames.reshape(frames.shape[0] * frames.shape[1], 2)
#
# # Plot Original and Framed Signal
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(signal)
# plt.title('Original Signal')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
# plt.subplot(2, 1, 2)
# plt.plot(np.concatenate(frames))
# plt.title('Framed Signal')
# plt.xlabel('Sample')
# plt.ylabel('Amplitude')
# plt.tight_layout()
# plt.show()
#

def frame_signal(frame_size, frame_overlap, window_type):
    # Divides the given signal into frames and applies a window function to each frame.
    # Returns the resulting frames as a 2D array, as well as the energy and zero-crossing rate of each frame.
    sample_rate, signal = read_audio_file()

    frame_length = int(round(frame_size * sample_rate))
    frame_step = int(round(frame_overlap * sample_rate))
    num_frames = int(np.ceil(float(np.abs(len(signal) - frame_length)) / frame_step))
    pad_signal_length = num_frames * frame_step + frame_length
    z = np.zeros(pad_signal_length - len(signal))
    pad_signal = np.append(signal, z)

    indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(
        np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
    frames = pad_signal[indices.astype(np.int32, copy=False)]

    if window_type == 'hamming':
        window = np.hamming(frame_length)
    elif window_type == 'hanning':
        window = np.hanning(frame_length)
    else:
        window = np.blackman(frame_length)
    frames *= window

    energy_list = np.sum(frames ** 2, axis=1)
    print("\n" + COLORS.BOLD_GREEN + "Energy Of Frames:" + COLORS.BOLD_PURPLE)
    print(energy_list)
    print(COLORS.RESET_COLOR)

    # the rate at which a signal transitions from positive to zero to negative or negative to zero to positive.
    zero_cross_list = np.array([np.sum(np.abs(np.diff(np.sign(frame)))) / (2 * len(frame)) for frame in frames])
    print("\n" + COLORS.BOLD_GREEN + "Zero Crossing Rate:" + COLORS.BOLD_PURPLE)
    print(zero_cross_list)
    print(COLORS.RESET_COLOR)

    return frames, energy_list, zero_cross_list

#
# def energy(frame):
#     """
#     Calculate energy of a frame
#     """
#     return sum(np.power(frame, 2))
#
#
# def zero_crossing(frame):
#     """
#     Calculate zero crossing rate of a frame
#     """
#     signs = np.sign(frame)
#     return np.sum(np.abs(signs[:-1] - signs[1:]) / 2)
#
#
# # Compute energy and zero crossing for each frame
# energies = np.apply_along_axis(energy, 1, frames)
# zero_crossings = np.apply_along_axis(zero_crossing, 1, frames)
#
# # Print the results
# print(COLORS.BOLD_CYAN + "Energies for each frame: \n" + COLORS.BOLD_GREEN)
# print(energies)
# print(COLORS.BOLD_CYAN + "\nZero crossing rates for each frame: \n" + COLORS.BOLD_GREEN)
# print(zero_crossings)
# print(COLORS.RESET_COLOR)
#
# # Plot energy and zero crossing for each frame
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(energies)
# plt.title('Energy for each frame')
# plt.xlabel('Frame')
# plt.ylabel('Energy')
# plt.subplot(2, 1, 2)
# plt.plot(zero_crossings)
# plt.title('Zero crossing rate for each frame')
# plt.xlabel('Frame')
# plt.ylabel('Zero crossing rate')
# plt.tight_layout()
# plt.show()

frame_size = float(input("Enter frame size in seconds: "))
frame_overlap = float(input("Enter overlap size in seconds: "))
window_type = input("Enter window type [e.g. hamming, hanning, blackman]: ")

frames, energy_list, zero_cross_list = frame_signal(frame_size, frame_overlap, window_type)

fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
ax1.plot((read_audio_file()[1]))
ax1.set_title('Original Signal')
ax2.plot(frames.reshape(-1))
ax2.set_title('Framed Signal')
plt.show()

plt.plot(energy_list)
plt.title('Energy of Frames')
plt.show()

plt.plot(zero_cross_list)
plt.title('Zero-Crossing Rate of Frames')
plt.show()

