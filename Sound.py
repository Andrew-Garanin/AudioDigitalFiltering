import copy
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

        self.first_channel = []
        self.second_channel = []

        self.upload_sound()

    def print_sound_info(self):
        sound_info = [f'Channels: {self.channels}', f'Sampling frequency: {self.frame_rate}',
                      f'Sample width: {self.sample_width}', f'Frames: {self.n_frames}']
        return sound_info

    def upload_sound(self):
        with wave.open(self.file_path, 'rb') as file:
            # self.save_wav_channel('file1.wav', file, 0)
            self.channels = file.getnchannels()
            self.frame_rate = file.getframerate()
            self.sample_width = file.getsampwidth()
            self.n_frames = file.getnframes()
            self.wav_data = np.fromstring(file.readframes(-1), np.int16)

            if self.channels == 2:
                self.first_channel = self.wav_data[0::2]
                self.second_channel = self.wav_data[1::2]

            # outwav = wave.open('file1.wav', 'w')
            # outwav.setparams(file.getparams())
            # outwav.setnchannels(1)
            # outwav.writeframes(self.second_channel.tostring())
            # outwav.close()

    def union_chanels(self):
        self.wav_data = []
        for index, (i, j) in enumerate(zip(self.first_channel, self.second_channel)):
            # self.first_channel[index] *= 0
            self.wav_data.append(self.first_channel[index])
            self.wav_data.append(self.second_channel[index])

        self.wav_data = np.asarray(self.wav_data)
        print('END!')

    def save_audio(self):
        with wave.open(os.path.join('output sounds', self.filter_name + '_' + ntpath.basename(self.file_path)),
                       'w') as new_file:
            new_file.setnchannels(self.channels)
            new_file.setsampwidth(self.sample_width)
            new_file.setframerate(self.frame_rate)
            new_file.writeframes(self.wav_data.tobytes())
            new_file.close()

    def play_sound(self):
        sd.play(self.wav_data, self.frame_rate * self.channels)

    def draw_graph(self):
        wav_data_copy = copy.deepcopy(self.wav_data)
        print(wav_data_copy)
        wav_data_copy.shape = -1, self.channels
        print(wav_data_copy)

        wav_data = wav_data_copy.T

        print(wav_data)
        # print(self.n_frames / float(self.frame_rate))
        step = 1 / float(self.frame_rate)

        t_seq = np.arange(0, self.n_frames / float(self.frame_rate), step)
        if self.channels == 1:
            fig = plt.figure()
            #plt.plot(t_seq, np.multiply(np.sign(wav_data[0]), 20*np.log10(np.abs(wav_data[0])/32768)))

            plt.plot(t_seq, wav_data[0])
            plt.xlabel("time (sec)")
            plt.ylabel("Амплитуда")
            fig.suptitle('Звуковая осцилограмма (моно)')

        elif self.channels == 2:
            fig, axs = plt.subplots(2)
            fig.suptitle('Звуковая осцилограмма (стерео)')
            fig.tight_layout()
            axs[0].plot(t_seq, wav_data[0])
            axs[1].plot(t_seq, wav_data[1])

            axs[0].set_title('L')
            #axs[0].yaxis.set_label_position("right")
            axs[0].set_ylabel('Амплитуда')
            axs[0].set_xlabel("time (sec)")

            axs[1].set_title('R')
            #axs[1].yaxis.set_label_position("right")
            axs[1].set_ylabel('Амплитуда')
            axs[1].set_xlabel("time (sec)")

        plt.show()
