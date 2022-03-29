from ui import mainForm

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QMenu, QMdiSubWindow, QMainWindow
import sounddevice as sd

import os
import wave, struct, math, random
import numpy as np
import matplotlib.pyplot as plt
import ntpath


def upload_sound(file_path):
    with wave.open(file_path, 'rb') as file:
        channels = file.getnchannels()
        frame_rate = file.getframerate()
        sample_width = file.getsampwidth()
        n_frames = file.getnframes()
        wav_data = np.fromstring(file.readframes(-1), np.int16)

        print('Channels', channels)
        print('Sampling frequency', frame_rate)
        print('Sample width', sample_width)
        print('Frames', n_frames)

        sound_info = dict()
        sound_info['wav_data'] = wav_data
        sound_info['channels'] = channels
        sound_info['frame_rate'] = frame_rate
        sound_info['sample_width'] = sample_width
        sound_info['n_frames'] = n_frames

        # ---------------------------------Для графика---------------------------------
        # print(wav_data)
        # wav_data.shape = -1, 2
        # print(wav_data)
        # wav_data = wav_data.T
        # print(wav_data)
        # print(n_frames/float(frame_rate))
        # duration = 1/float(frame_rate)
        #
        # t_seq = np.arange(0, n_frames/float(frame_rate), duration)
        # plt.plot(t_seq, wav_data[0])
        # plt.show()
        return sound_info


def play_sound_stream(sound_info):
    sd.play(sound_info['wav_data'], sound_info['frame_rate'] * sound_info['channels'])


def stop_sound_stream():
    sd.stop()


def save_file(sound_info, file_name):
    obj = wave.open(os.path.join('output sounds', 'distortion_' + ntpath.basename(file_name)), 'w')
    obj.setnchannels(sound_info['channels'])  # stereo
    obj.setsampwidth(sound_info['sample_width'])
    obj.setframerate(sound_info['frame_rate'])
    obj.writeframes(sound_info['wav_data'].tobytes())
    obj.close()


def create_sound_distortion_filter(sound_info):
    blend = 2
    drive = 5
    range1 = 5
    volume = 4
    for i, value in enumerate(sound_info['wav_data']):
        # if i % 2 == 0:
        sound_info['wav_data'][i] = (((((2 / math.pi) * math.atan(
            sound_info['wav_data'][i] * drive * range1)) * blend) + (
                                              sound_info['wav_data'][i] * (1 - blend))) / 2) * volume
    print('Звук создан')
    return sound_info
    # ---------------------------------Для графика---------------------------------
    # print(sound_info['wav_data'])
    # sound_info['wav_data'].shape = -1, 2
    # print(sound_info['wav_data'])
    # wav_data = sound_info['wav_data'].T
    # print(wav_data)
    # print(sound_info['n_frames'] / float(sound_info['frame_rate']))
    # duration = 1 / float(sound_info['frame_rate'])
    #
    # t_seq = np.arange(0, sound_info['n_frames'] / float(sound_info['frame_rate']), duration)
    # plt.plot(t_seq, wav_data[0])\\
    # plt.show()


def create_sound_echo_filter(sound_info):
    blend = 2
    drive = 5
    range1 = 5
    volume = 15
    ms5 = math.floor(sound_info['frame_rate'] / 1000) * 5
    array = sound_info['wav_data'].copy()
    time_delay = math.floor(sound_info['frame_rate'] / 2)
    for i, value in enumerate(sound_info['wav_data']):
        if i + time_delay < len(sound_info['wav_data']):
            sound_info['wav_data'][i + time_delay] += (array[i] + array[i - ms5] + array[i + ms5]) / 3 * 0.7
    print('Звук создан')


def create_sound_pop_click_remove_filter(sound_info):
    pass


class MyQtApp(mainForm.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.sound_info = {"wav_data": [],
                           'channels': int,
                           'frame_rate': int,
                           'sample_width': int,
                           'n_frames': int,
                           }
        # -----------------------------Привязка методов к кнопкам---------------------------
        self.toolButtonFilePath.clicked.connect(self.choose_file_path)
        self.pushButtonApplyFilter.clicked.connect(self.apply_distortion)
        self.buttonPlay.clicked.connect(self.play_sound)
        self.buttonStop.clicked.connect(stop_sound_stream)
        self.buttonSave.clicked.connect(self.save_audio)

    def choose_file_path(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.wav')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                self.lineEditFilePath.setText(file.name)
                self.sound_info = upload_sound(file.name)

    def apply_distortion(self):
        # self.sound_info = create_sound_distortion_filter(self.sound_info)
         create_sound_distortion_filter(self.sound_info)
        # create_sound_echo_filter(sound_info, file_name)
        #self.sound_info = create_sound_pop_click_remove_filter(self.sound_info)

    def play_sound(self):
        play_sound_stream(self.sound_info)

    def save_audio(self):
        file_name = self.lineEditFilePath.text()
        sound_info = upload_sound(file_name)

        save_file(self.sound_info, file_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
