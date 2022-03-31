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

    def choose_file_path(self):
        file_path, ext = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', filter='*.wav')
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as file:
                self.lineEditFilePath.setText(file.name)
                self.original_sound = Sound(file.name)

    def apply_filter_distortion(self):
        pass
        self.filtered_sound = sound_filters.create_sound_distortion_filter(self.original_sound, self.get_blend_value(),
                                                                           self.get_drive_value(),
                                                                           self.get_range_value(),
                                                                           self.get_volume_value())
        # self.sound_info = create_sound_echo_filter(self.sound_info)
        # self.sound_info = create_speed_up(self.sound_info)
        # self.sound_info = create_slow_down(self.sound_info)
        # self.sound_info = create_sound_pop_click_remove_filter(self.sound_info)

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


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
