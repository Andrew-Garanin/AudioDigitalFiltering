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
        self.print_sound_info()

    def print_sound_info(self):
        print(colored('-----------------------Sound info-----------------------', 'green'))
        print('Channels', self.channels)
        print('Sampling frequency', self.frame_rate)
        print('Sample width', self.sample_width)
        print('Frames', self.n_frames)
        print()

    def save_wav_channel(self, fn, wav, channel):
        '''
        Take Wave_read object as an input and save one of its
        channels into a separate .wav file.
        '''
        # Read data
        nch = wav.getnchannels()
        depth = wav.getsampwidth()
        wav.setpos(0)
        sdata = wav.readframes(wav.getnframes())

        # Extract channel data (24-bit data not supported)
        typ = {1: np.uint8, 2: np.uint16, 4: np.uint32}.get(depth)
        if not typ:
            raise ValueError("sample width {} not supported".format(depth))
        if channel >= nch:
            raise ValueError("cannot extract channel {} out of {}".format(channel + 1, nch))
        print("Extracting channel {} out of {} channels, {}-bit depth".format(channel + 1, nch, depth * 8))
        data = np.fromstring(sdata, dtype=typ)
        ch_data = data[channel::nch]

        # Save channel to a separate file
        outwav = wave.open(fn, 'w')
        outwav.setparams(wav.getparams())
        outwav.setnchannels(1)
        outwav.writeframes(ch_data.tostring())
        outwav.close()


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
        for i, j in zip(self.first_channel, self.second_channel):
            self.wav_data.append(i)
            self.wav_data.append(j)
        # for i,value in enumerate(self.first_channel):
        #     self.wav_data.append(self.first_channel[i])
        #     self.wav_data.append(0)

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
