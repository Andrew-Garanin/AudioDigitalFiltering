import math
import ntpath
import os
import wave

import numpy as np
import sounddevice as sd
from PySide2 import QtWidgets
from matplotlib import pyplot as plt
from ui import mainForm


def create_sound_distortion_filter(sound_info):
    blend = 2
    drive = 5
    range1 = 5
    volume = 10
    for i, value in enumerate(sound_info['wav_data']):
        # if i % 2 == 0:
        sound_info['wav_data'][i] = (((((2 / math.pi) * math.atan(
            sound_info['wav_data'][i] * drive * range1)) * blend) + (
                                              sound_info['wav_data'][i] * (1 - blend))) / 2) * volume
    print('Звук создан')
    return sound_info


def create_speed_up(sound_info):
    temp = np.array(sound_info['wav_data'])
    print(len(temp))
    # factor_length - is a percentage of original size to some value. example 75% (been 20 samples -> will be 15)
    factor_length = 0.8
    # x1 / x1-x2 = step_length
    x1 = len(temp)
    x2 = x1 * factor_length
    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (x1 / (x1 - x2)) * sound_info['channels']
    i = len(sound_info['wav_data']) - 1
    while i > 2:
        floored_index = math.floor(i)
        temp = np.delete(temp, floored_index)
        temp = np.delete(temp, floored_index - 1)

        i -= step_length
    print('final factor_length: ', len(temp) / x1)
    print('final len: ', len(temp))
    sound_info['wav_data'] = temp
    print('Sound created!')
    return sound_info


def create_slow_down(sound_info):
    initial_time = datetime.datetime.now()

    # factor_length - is a percentage of original size to some value. example 130% (been 20 samples -> will be 26)
    factor_length = 2

    x1 = len(sound_info['wav_data'])
    x2 = math.floor(x1 * factor_length)

    temp = np.array(sound_info['wav_data'])

    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (x1 / (x2 - x1)) * sound_info['channels']
    print('step_length', step_length)
    i = len(sound_info['wav_data']) - 1
    while i > 4:
        floored_index = math.floor(i)
        if floored_index % 10000 < 50:
            print("all good: ", floored_index)

        # value1 = (temp[floored_index] + temp[floored_index - 1]) / 2
        # floored_index -= 1
        # value2 = (temp[floored_index] + temp[floored_index - 1]) / 2

        value1 = temp[floored_index]
        floored_index -= 1
        value2 = temp[floored_index]

        temp = np.insert(temp, floored_index, value1)
        temp = np.insert(temp, floored_index, value2)

        i -= step_length

    sound_info['wav_data'] = temp
    print('time', datetime.datetime.now() - initial_time)
    print('final factor_length: ', len(temp) / x1)
    print('final len: ', len(temp))
    print('Sound created!')
    return sound_info


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
    return sound_info


def create_sound_pop_click_remove_filter(sound_info):
    fade = 10

    for i, sample in enumerate(sound_info['wav_data']):
        if i + 1 < len(sound_info['wav_data']) and math.fabs(
                sound_info['wav_data'][i] - sound_info['wav_data'][i + 1]) > 5000:
            fade_in = np.arange(0.2, 1., 0.8 / fade)
            fade_out = np.arange(1., 0.2, -0.8 / fade)
            problem_sample = i
            print(i)

            sound_info['wav_data'][(problem_sample - fade):(problem_sample)] = np.multiply(
                sound_info['wav_data'][(problem_sample - fade):(problem_sample)], fade_out)
            sound_info['wav_data'][problem_sample:(problem_sample + fade)] = np.multiply(
                sound_info['wav_data'][problem_sample:(problem_sample + fade)], fade_in)
    print('Звук создан')
    return sound_info


class MyQtApp(mainForm.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.sound_info = dict()

        # -----------------------------Wheels-----------------------------
        self.blendWheel.setValue(2)
        self.blendWheel.valueChanged.connect(self.blendMoved)

        self.driveWheel.setValue(2)
        self.driveWheel.valueChanged.connect(self.driveMoved)

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.toolButtonFilePath.clicked.connect(self.choose_file_path)
        self.pushButtonApplyFilter.clicked.connect(self.apply_filter)
        self.buttonPlay.clicked.connect(self.play_sound)
        self.buttonStop.clicked.connect(self.stop_sound)
        self.buttonSave.clicked.connect(self.save_audio)
        self.buttonGraph.clicked.connect(self.draw_graph)

    def blendMoved(self):
        print("Dial value = %i" % (self.blendWheel.value()))

    def driveMoved(self):
        print("Drive value = %i" % (self.blendWheel.value()))

    def choose_file_path(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.wav')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                self.lineEditFilePath.setText(file.name)
                self.sound_info = self.upload_sound(file.name)

    def apply_filter(self):
        pass
        # self.sound_info = create_sound_distortion_filter(self.sound_info)
        # self.sound_info = create_sound_echo_filter(self.sound_info)
        # self.sound_info = create_speed_up(self.sound_info)
        # self.sound_info = create_slow_down(self.sound_info)
        self.sound_info = create_sound_pop_click_remove_filter(self.sound_info)

    def play_sound(self):
        sd.play(self.sound_info['wav_data'], self.sound_info['frame_rate'] * self.sound_info['channels'])

    def stop_sound(self):
        sd.stop()

    def save_audio(self):
        file_name = self.lineEditFilePath.text()
        obj = wave.open(os.path.join('output sounds', 'distortion_' + ntpath.basename(file_name)), 'w')
        obj.setnchannels(self.sound_info['channels'])
        obj.setsampwidth(self.sound_info['sample_width'])
        obj.setframerate(self.sound_info['frame_rate'])
        obj.writeframes(self.sound_info['wav_data'].tobytes())
        obj.close()

    def upload_sound(self, file_path):
        with wave.open(file_path, 'rb') as file:
            channels = file.getnchannels()
            frame_rate = file.getframerate()
            sample_width = file.getsampwidth()
            n_frames = file.getnframes()
            wav_data = np.fromstring(file.readframes(-1), np.int16)

            sound_info = dict()
            sound_info['wav_data'] = wav_data
            sound_info['channels'] = channels
            sound_info['frame_rate'] = frame_rate
            sound_info['sample_width'] = sample_width
            sound_info['n_frames'] = n_frames

            # ---------------------------------Print sound info---------------------------------
            print('Channels', channels)
            print('Sampling frequency', frame_rate)
            print('Sample width', sample_width)
            print('Frames', n_frames)

            return sound_info

    def draw_graph(self):
        # print(wav_data)
        self.sound_info['wav_data'].shape = -1, 2
        # print(wav_data)
        wav_data = self.sound_info['wav_data'].T
        # print(wav_data)
        print(self.sound_info['n_frames'] / float(self.sound_info['frame_rate']))
        duration = 1 / float(self.sound_info['frame_rate'])

        t_seq = np.arange(0, self.sound_info['n_frames'] / float(self.sound_info['frame_rate']), duration)
        plt.plot(t_seq, wav_data[0])
        plt.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
