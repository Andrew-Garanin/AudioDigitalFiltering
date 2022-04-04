import math

import numpy as np
import sounddevice as sd
from PySide2 import QtWidgets

# from denoise import removeNoise, band_limited_noise
from ui import mainForm
from Sound import Sound

import sound_filters
from res import res_file


def stop_sound():
    sd.stop()


class MyQtApp(mainForm.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        res_file.qInitResources()

        self.original_sound = None
        self.filtered_sound = None

        # -----------------------------Distortion Wheels-----------------------------
        self.blendWheel.setValue(0)
        self.blendWheel.valueChanged.connect(self.blendMoved)
        self.blendLabelValue.setText(str(self.get_blend_value()))

        self.driveWheel.setValue(0)
        self.driveWheel.valueChanged.connect(self.driveMoved)
        self.driveLabelValue.setText(str(self.get_drive_value()))

        self.rangeWheel.setValue(0)
        self.rangeWheel.valueChanged.connect(self.rangeMoved)
        self.rangeLabelValue.setText(str(self.get_range_value()))

        self.volumeWheel.setValue(100)
        self.volumeWheel.valueChanged.connect(self.volumeMoved)
        self.volumeLabelValue.setText(str(self.get_volume_value()))

        # -----------------------------Echo Wheels-----------------------------
        self.delayTimeWheel.setValue(0)
        self.delayTimeWheel.valueChanged.connect(self.delayTimeMoved)
        self.delayTimeLabelValue.setText(self.get_delay_time_string())

        self.echoLevelWheel.setValue(0)
        self.echoLevelWheel.valueChanged.connect(self.echoLevelMoved)
        self.echoLevelLabelValue.setText(self.get_echo_level_string())

        self.blurIntervalWheel.setValue(0)
        self.blurIntervalWheel.valueChanged.connect(self.blurIntervalMoved)
        self.blurIntervalLabelValue.setText(str(self.get_blur_interval_string()))

        # -----------------------------Removing Clicks And Pops Wheels-----------------------------
        self.sensitivityWheel.setValue(0)
        self.sensitivityWheel.valueChanged.connect(self.sensitivityMoved)
        self.sensitivityLabelValue.setText(self.get_sensitivity_string())

        self.fadeLengthWheel.setValue(0)
        self.fadeLengthWheel.valueChanged.connect(self.fadeLengthMoved)
        self.fadeLengthLabelValue.setText(self.get_fade_length_string())

        self.mutePowerWheel.setValue(0)
        self.mutePowerWheel.valueChanged.connect(self.mutePowerMoved)
        self.mutePowerLabelValue.setText(self.get_mute_power_string())

        # -----------------------------Time Slider-----------------------------
        self.timeSlider.setValue(100)
        self.timeLabelValue.setText(self.get_time_string())
        self.timeSlider.valueChanged.connect(self.timeSliderMoved)

        # -----------------------------Remove Silence Wheels-----------------------------
        self.offsetSamplesWheel.setValue(100)
        self.offsetSamplesLabelValue.setText(str(self.get_offset_samples_value()))
        self.offsetSamplesWheel.valueChanged.connect(self.offsetSamplesMoved)

        self.aggressionWheel.setValue(10)
        self.aggressionLabelValue.setText(str(self.get_aggression_value()))
        self.aggressionWheel.valueChanged.connect(self.aggressionMoved)

        # -----------------------------Fade Wheels-----------------------------
        self.leftFadeLengthWheel.setValue(4)
        self.leftFadeLengthLableValue.setText(str(self.get_left_fade_length_value_sec()))
        self.leftFadeLengthWheel.valueChanged.connect(self.leftFadeLengthMoved)

        self.leftFadeStrenghtWheel.setValue(2)
        self.leftFadeStrenghtLabelValue.setText(str(self.get_left_fade_strenght_value()))
        self.leftFadeStrenghtWheel.valueChanged.connect(self.leftFadeStrenghtMoved)

        self.rightFadeLengthWheel.setValue(4)
        self.rightFadeLengthLableValue.setText(str(self.get_right_fade_length_value_sec()))
        self.rightFadeLengthWheel.valueChanged.connect(self.rightFadeLengthMoved)

        self.rightFadeStrenghtWheel.setValue(2)
        self.rightFadeStrenghtLabelValue.setText(str(self.get_right_fade_strenght_value()))
        self.rightFadeStrenghtWheel.valueChanged.connect(self.rightFadeStrenghtMoved)

        # -----------------------------Привязка методов к кнопкам---------------------------
        self.buttonSelectFile.clicked.connect(self.choose_file_path)
        self.buttonPlayOriginalSound.clicked.connect(self.play_original_sound)
        self.buttonPlayFilteredSound.clicked.connect(self.play_filtered_sound)
        self.buttonStop.clicked.connect(stop_sound)
        self.buttonSave.clicked.connect(self.save_audio)
        self.buttonGraphOriginal.clicked.connect(self.draw_graph_original)
        self.buttonGraphFiltered.clicked.connect(self.draw_graph_filtered)

        # -----------------------------Кнопки фильтров-----------------------------
        self.buttonFilterDistortion.clicked.connect(self.apply_filter_distortion)
        self.buttonFilterEcho.clicked.connect(self.apply_filter_echo)
        self.buttonFilterRemovingClicksAndPops.clicked.connect(self.apply_filter_removing_click_pop)
        self.buttonFilterTime.clicked.connect(self.apply_filter_time)
        self.buttonFilterRemoveSilence.clicked.connect(self.apply_filter_silence)
        self.buttonFilterFade.clicked.connect(self.apply_fade_in_fade_out_filter)

    # -----------------------------Distortion Wheels utils-----------------------------
    def get_blend_value(self):
        return self.blendWheel.value() / 10000

    def get_drive_value(self):
        return self.driveWheel.value() / 10000

    def get_range_value(self):
        return self.rangeWheel.value()

    def get_volume_value(self):
        return self.volumeWheel.value() / 100

    def blendMoved(self):
        self.blendLabelValue.setText(str(self.get_blend_value()))

    def driveMoved(self):
        self.driveLabelValue.setText(str(self.get_drive_value()))

    def rangeMoved(self):
        self.rangeLabelValue.setText(str(self.get_range_value()))

    def volumeMoved(self):
        self.volumeLabelValue.setText(str(self.get_volume_value()))

    # -----------------------------Echo Wheels utils-----------------------------
    def get_delay_time_value(self):
        return self.delayTimeWheel.value() / 100

    def get_echo_level_value(self):
        return self.echoLevelWheel.value() / 100

    def get_blur_interval_value(self):
        return self.blurIntervalWheel.value()

    def delayTimeMoved(self):
        self.delayTimeLabelValue.setText(self.get_delay_time_string())

    def echoLevelMoved(self):
        self.echoLevelLabelValue.setText(self.get_echo_level_string())

    def blurIntervalMoved(self):
        self.blurIntervalLabelValue.setText(self.get_blur_interval_string())

    def get_delay_time_string(self):
        return str(self.get_delay_time_value()) + ' sec'

    def get_echo_level_string(self):
        return str(int(self.get_echo_level_value() * 100)) + '%'

    def get_blur_interval_string(self):
        return str(int(self.get_blur_interval_value()))

    # -----------------------------Removing Clicks And Pops Wheels utils-----------------------------
    def get_sensitivity_value(self):
        return self.sensitivityWheel.value() * 1000

    def get_fade_length_value(self):
        return self.fadeLengthWheel.value()

    def get_mute_power_value(self):
        return self.mutePowerWheel.value()

    def sensitivityMoved(self):
        self.sensitivityLabelValue.setText(self.get_sensitivity_string())

    def fadeLengthMoved(self):
        self.fadeLengthLabelValue.setText(self.get_fade_length_string())

    def mutePowerMoved(self):
        self.mutePowerLabelValue.setText(self.get_mute_power_string())

    def get_sensitivity_string(self):
        return str(self.get_sensitivity_value())

    def get_fade_length_string(self):
        return str(self.get_fade_length_value()) + ' samples'

    def get_mute_power_string(self):
        return str(self.get_mute_power_value())

    # -----------------------------Time Slider utils-----------------------------
    def get_time_value(self):
        return self.timeSlider.value()

    def get_time_shrink_value(self):
        return self.get_time_value() / 100

    def get_time_string(self):
        return str(self.get_time_value()) + "%"

    def timeSliderMoved(self):
        self.timeLabelValue.setText(self.get_time_string())

    # -----------------------------Silence Remover Wheels utils-----------------------------
    def get_offset_samples_value(self):
        return self.offsetSamplesWheel.value() * 100

    def offsetSamplesMoved(self):
        self.offsetSamplesLabelValue.setText(str(self.get_offset_samples_value()))

    def get_aggression_value(self):
        return self.aggressionWheel.value() * 50

    def aggressionMoved(self):
        self.aggressionLabelValue.setText(str(self.get_aggression_value()))

    # -----------------------------Fade Wheels utils-----------------------------
    def get_left_fade_length_value_sec(self):
        return self.leftFadeLengthWheel.value() / 10

    def get_left_fade_length_value(self):
        return math.floor(self.get_left_fade_length_value_sec() * self.original_sound.frame_rate)

    def leftFadeLengthMoved(self):
        self.leftFadeLengthLableValue.setText(str(self.get_left_fade_length_value_sec()))

    def get_left_fade_strenght_value(self):
        return self.leftFadeStrenghtWheel.value()

    def leftFadeStrenghtMoved(self):
        self.leftFadeStrenghtLabelValue.setText(str(self.get_left_fade_strenght_value()))

    # ---------------RIGHT----------------

    def get_right_fade_length_value_sec(self):
        return self.rightFadeLengthWheel.value() / 10

    def get_right_fade_length_value(self):
        return math.floor(self.get_right_fade_length_value_sec() * self.original_sound.frame_rate)

    def rightFadeLengthMoved(self):
        self.rightFadeLengthLableValue.setText(str(self.get_right_fade_length_value_sec()))

    def get_right_fade_strenght_value(self):
        return self.rightFadeStrenghtWheel.value()

    def rightFadeStrenghtMoved(self):
        self.rightFadeStrenghtLabelValue.setText(str(self.get_right_fade_strenght_value()))

    # -----------------------------Apply Filters Methods-----------------------------
    def apply_filter_distortion(self):
        self.filtered_sound = sound_filters.create_sound_distortion_filter(self.original_sound, self.get_blend_value(),
                                                                           self.get_drive_value(),
                                                                           self.get_range_value(),
                                                                           self.get_volume_value())

    def apply_filter_echo(self):
        self.filtered_sound = sound_filters.create_sound_echo_filter(self.original_sound, self.get_delay_time_value(),
                                                                     self.get_echo_level_value(),
                                                                     self.get_blur_interval_value())

    def apply_filter_removing_click_pop(self):
        self.filtered_sound = sound_filters.create_sound_pop_click_remove_filter(self.original_sound,
                                                                                 self.get_sensitivity_value(),
                                                                                 self.get_fade_length_value(),
                                                                                 self.get_mute_power_value())

    def apply_filter_time(self):
        shrink_val = self.get_time_shrink_value()

        if shrink_val > 1:
            self.filtered_sound = sound_filters.create_slow_down(self.original_sound, shrink_val)
        else:
            self.filtered_sound = sound_filters.create_speed_up(self.original_sound, shrink_val)

    def apply_filter_silence(self):
        self.filtered_sound = sound_filters.create_remove_silence_filter(self.original_sound,
                                                                         self.get_offset_samples_value(),
                                                                         self.get_aggression_value())

    def apply_fade_in_fade_out_filter(self):
        self.filtered_sound = sound_filters.fade_in_fade_out(self.original_sound,
                                                             self.get_left_fade_length_value(),
                                                             self.get_left_fade_strenght_value(),
                                                             self.get_right_fade_length_value(),
                                                             self.get_right_fade_strenght_value())

    # -----------------------------Other Methods-----------------------------
    def play_original_sound(self):
        self.original_sound.play_sound()

    def play_filtered_sound(self):
        # self.filtered_sound = copy.deepcopy(self.original_sound)
        # self.filtered_sound.wav_data = self.filtered_sound.wav_data/32768
        # noise_len = 2  # seconds
        # noise = band_limited_noise(min_freq=4000, max_freq=12000, samples=len(self.original_sound.wav_data),
        #                            samplerate=self.original_sound.frame_rate)
        # noise_clip = self.filtered_sound.wav_data[70560:82017]

        # self.filtered_sound.wav_data = audio_clip_band_limited
        # self.filtered_sound.play_sound()
        # IPython.display.Audio(data=audio_clip_band_limited, rate=self.original_sound.frame_rate)

        # self.filtered_sound.wav_data = removeNoise(audio_clip=self.filtered_sound.wav_data, noise_clip=noise_clip)

        # IPython.display.Audio(data=audio_clip_band_limited, rate=self.original_sound.frame_rate)
        # self.filtered_sound.wav_data = self.filtered_sound.wav_data*32768
        # print(self.filtered_sound.wav_data)
        # self.filtered_sound.wav_data = np.floor(self.filtered_sound.wav_data)
        self.filtered_sound.play_sound()

    def save_audio(self):
        self.filtered_sound.save_audio()

    def draw_graph_original(self):
        self.original_sound.draw_graph()

    def draw_graph_filtered(self):
        self.filtered_sound.draw_graph()

    def choose_file_path(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.wav')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                self.lineEditFilePath.setText(file.name)
                self.original_sound = Sound(file.name)
                self.soundInfoList.clear()
                sound_info = self.original_sound.print_sound_info()
                self.soundInfoList.addItems(sound_info)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
