import ntpath
import os
import wave

import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt
from termcolor import colored


class Sound:
    def __init__(self, file_path):
        self.file_path = file_path

        # ---------------------------------Sound info---------------------------------
        self.channels = None
        self.frame_rate = None
        self.sample_width = None
        self.n_frames = None
        self.wav_data = None
        self.filter_name = ''

        self.upload_sound()
        self.print_sound_info()

    def print_sound_info(self):
        print(colored('-----------------------Sound info-----------------------', 'green'))
        print('Channels', self.channels)
        print('Sampling frequency', self.frame_rate)
        print('Sample width', self.sample_width)
        print('Frames', self.n_frames)
        print()

    def upload_sound(self):
        with wave.open(self.file_path, 'rb') as file:
            self.channels = file.getnchannels()
            self.frame_rate = file.getframerate()
            self.sample_width = file.getsampwidth()
            self.n_frames = file.getnframes()
            self.wav_data = np.fromstring(file.readframes(-1), np.int16)

    def save_audio(self):
        with wave.open(os.path.join('output sounds', self.filter_name + '_' + ntpath.basename(self.file_path)), 'w') as new_file:
            new_file.setnchannels(self.channels)
            new_file.setsampwidth(self.sample_width)
            new_file.setframerate(self.frame_rate)
            new_file.writeframes(self.wav_data.tobytes())
            new_file.close()

    def play_sound(self):
        sd.play(self.wav_data, self.frame_rate * self.channels)

    def draw_graph(self):
        # print(wav_data)
        self.wav_data.shape = -1, 2
        # print(wav_data)
        wav_data = self.wav_data.T
        # print(wav_data)
        # print(self.n_frames / float(self.frame_rate))
        duration = 1 / float(self.frame_rate)

        t_seq = np.arange(0, self.n_frames / float(self.frame_rate), duration)
        plt.plot(t_seq, wav_data[0])
        plt.show()
