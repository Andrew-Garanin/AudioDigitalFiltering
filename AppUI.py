import asyncio

from ui import mainForm

from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QMenu, QMdiSubWindow, QMainWindow
import sounddevice as sd
import os
import wave, struct, math, random
import numpy as np
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


def create_sound_distortion_filter(sound_info):
    blend = 2
    drive = 5
    range1 = 5
    volume = 15
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
    # plt.plot(t_seq, wav_data[0])
    # plt.show()


def create_speed_up(sound_info):
    temp = np.array(sound_info['wav_data'])
    print(len(temp))
    # TODO: rename криветка into some better
    shrimp = 0.75  # shirm original size to 75% (been 20 samples -> will be 15)
    # x1 / x1-x2 = step_length
    x1 = len(temp)
    x2 = x1 * shrimp
    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (x1 / (x1 - x2)) * sound_info['channels']
    i = len(sound_info['wav_data']) - 1
    while i > 2:
        floored_index = math.floor(i)
        temp = np.delete(temp, floored_index)
        temp = np.delete(temp, floored_index - 1)

        i -= step_length
    print('final shrim: ', len(temp) / x1)
    print('final len: ', len(temp))
    sound_info['wav_data'] = temp
    print('Sound created!')
    return sound_info

# TODO: tested for Дребезжание***
def create_slow_down(sound_info):
    temp = np.array(sound_info['wav_data'])
    print(len(temp))
    # TODO: rename криветка into some better
    shrimp = 1.3  # shirm original size to 130% (been 20 samples -> will be 26)
    # x1 / x1-x2 = step_length
    x1 = len(temp)
    x2 = x1 / shrimp
    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (x1 / (x1 - x2)) * sound_info['channels']
    i = len(sound_info['wav_data']) - 1
    while i > 4:
        floored_index = math.floor(i)
        value1 = (temp[floored_index] + temp[floored_index - 1]) / 2

        floored_index -= 1
        value2 = (temp[floored_index] + temp[floored_index - 1]) / 2

        # np.insert(temp, [floored_index, floored_index+1], [value2, value1])
        temp = np.insert(temp, floored_index, value1)
        temp = np.insert(temp, floored_index, value2)

        i -= step_length

    print('final shrim: ', len(temp) / x1)
    print('final len: ', len(temp))
    sound_info['wav_data'] = temp
    print('Sound created!')
    return sound_info


def save_file(sound_info, file_name):
    obj = wave.open(os.path.join('output sounds', 'distortion_' + ntpath.basename(file_name)), 'w')
    obj.setnchannels(sound_info['channels'])  # stereo
    obj.setsampwidth(sound_info['sample_width'])
    obj.setframerate(sound_info['frame_rate'])
    obj.writeframes(sound_info['wav_data'].tobytes())
    obj.close()


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


def tone(sound_info):
    # self, frequency, length = 1000, play = False,
    # number_of_frames = int(self.bitrate * length/1000.)
    new_array = []
    bit_rate = sound_info['frame_rate'] * 16 * 2
    record = False
    x = 0
    y = 0
    while 1:
        x += 1
        v = math.sin(x / ((bit_rate / float(sound_info['frame_rate'])) / math.pi))

        # Find where the sin tip starts.
        if round(v, 3) == +1:
            record = True

        if record:
            new_array.append(v * 127 + 128)
            y += 1
            if y > sound_info['n_frames'] and round(v, 3) == +1:
                # Always end on the high tip of the sin wave to clips align.
                break
    print('Звук создан')


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
        # self.pushButtonApplyFilter.
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
        # self.sound_info = create_speed_up(self.sound_info)
        self.sound_info = create_slow_down(self.sound_info)
        # create_sound_distortion_filter(sound_info, file_name)
        # create_sound_echo_filter(sound_info, file_name)
        # tone(self.sound_info)

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
