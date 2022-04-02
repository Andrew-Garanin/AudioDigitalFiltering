import sounddevice as sd
from PySide2 import QtWidgets
from ui import mainForm
from Sound import Sound

import sound_filters


def stop_sound():
    sd.stop()


class MyQtApp(mainForm.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

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
        self.blendLabelValue.setText(str(self.get_delay_time_value()))

        self.echoLevelWheel.setValue(0)
        self.echoLevelWheel.valueChanged.connect(self.echoLevelMoved)
        self.echoLevelLabelValue.setText(str(self.get_echo_level_value()))

        self.blurIntervalWheel.setValue(0)
        self.blurIntervalWheel.valueChanged.connect(self.blurIntervalMoved)
        self.blurIntervalLabelValue.setText(str(self.get_blur_interval_value()))

        # -----------------------------Removing Clicks And Pops Wheels-----------------------------
        self.sensitivityWheel.setValue(0)
        self.sensitivityWheel.valueChanged.connect(self.sensitivityMoved)
        self.sensitivityLabelValue.setText(str(self.get_sensitivity_value()))

        self.fadeLengthWheel.setValue(0)
        self.fadeLengthWheel.valueChanged.connect(self.fadeLengthMoved)
        self.fadeLengthLabelValue.setText(str(self.get_fade_length_value()))

        self.mutePowerWheel.setValue(0)
        self.mutePowerWheel.valueChanged.connect(self.mutePowerMoved)
        self.mutePowerLabelValue.setText(str(self.get_mute_power_value()))
        # -----------------------------Removing Clicks And Pops Wheels-----------------------------
        self.sensitivityWheel.setValue(0)
        self.sensitivityWheel.valueChanged.connect(self.sensitivityMoved)
        self.sensitivityLabelValue.setText(str(self.get_sensitivity_value()))

        self.fadeLengthWheel.setValue(0)
        self.fadeLengthWheel.valueChanged.connect(self.fadeLengthMoved)
        self.fadeLengthLabelValue.setText(str(self.get_fade_length_value()))

        self.mutePowerWheel.setValue(0)
        self.mutePowerWheel.valueChanged.connect(self.mutePowerMoved)
        self.mutePowerLabelValue.setText(str(self.get_mute_power_value()))

        # -----------------------------Time Slider-----------------------------
        self.timeSlider.setValue(100)
        self.blendLabelValue.setText(self.get_time_string())
        self.timeSlider.valueChanged.connect(self.timeSliderMoved)

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
        print( self.echoLevelWheel.value() / 100)
        return self.echoLevelWheel.value() / 100

    def get_blur_interval_value(self):
        print(self.blurIntervalWheel.value())
        return self.blurIntervalWheel.value()

    def delayTimeMoved(self):
        self.delayTimeLabelValue.setText(str(self.get_delay_time_value()))

    def echoLevelMoved(self):
        self.echoLevelLabelValue.setText(str(int(self.get_echo_level_value() * 100)))

    def blurIntervalMoved(self):
        self.blurIntervalLabelValue.setText(str(self.get_blur_interval_value()))

    # -----------------------------Removing Clicks And Pops Wheels utils-----------------------------
    def get_sensitivity_value(self):
        return self.sensitivityWheel.value() * 1000

    def get_fade_length_value(self):
        return self.fadeLengthWheel.value()

    def get_mute_power_value(self):
        return self.mutePowerWheel.value()

    def sensitivityMoved(self):
        self.sensitivityLabelValue.setText(str(self.get_sensitivity_value()))

    def fadeLengthMoved(self):
        self.fadeLengthLabelValue.setText(str(self.get_fade_length_value()))

    def mutePowerMoved(self):
        self.mutePowerLabelValue.setText(str(self.get_mute_power_value()))

    # -----------------------------Time Slider utils-----------------------------
    def get_time_value(self):
        return self.timeSlider.value()

    def get_time_shrink_value(self):
        return self.get_time_value() / 100

    def get_time_string(self):
        return str(self.get_time_value()) + "%"

    def timeSliderMoved(self):
        self.timeLabelValue.setText(self.get_time_string())
    # -----------------------------Removing Clicks And Pops Wheels utils-----------------------------
    def get_sensitivity_value(self):
        return self.sensitivityWheel.value() * 1000

    def get_fade_length_value(self):
        return self.fadeLengthWheel.value()

    def get_mute_power_value(self):
        return self.mutePowerWheel.value()

    def sensitivityMoved(self):
        self.sensitivityLabelValue.setText(str(self.get_sensitivity_value()))

    def fadeLengthMoved(self):
        self.fadeLengthLabelValue.setText(str(self.get_fade_length_value()))

    def mutePowerMoved(self):
        self.mutePowerLabelValue.setText(str(self.get_mute_power_value()))

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
        self.filtered_sound.union_chanels()

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

    # -----------------------------Other Methods-----------------------------
    def play_original_sound(self):
        self.original_sound.play_sound()

    def play_filtered_sound(self):
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


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
