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


def create_sound_distortion_filter(sound_info, file_name):
    blend = 2
    drive = 5
    range1 = 5
    volume = 15
    for i, value in enumerate(sound_info['wav_data']):
        # if i % 2 == 0:
        sound_info['wav_data'][i] = (((((2 / math.pi) * math.atan(
            sound_info['wav_data'][i] * drive * range1)) * blend) + (
                                              sound_info['wav_data'][i] * (1 - blend))) / 2) * volume

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

    obj = wave.open(os.path.join('output sounds', ntpath.basename(file_name + '_distortion')), 'w')
    obj.setnchannels(sound_info['channels'])  # stereo
    obj.setsampwidth(sound_info['sample_width'])
    obj.setframerate(sound_info['frame_rate'])
    obj.writeframes(sound_info['wav_data'].tobytes())
    obj.close()


if __name__ == '__main__':
    # sound_info = upload_sound('jopa.wav')
    file_name = 'input sounds/Directed_by_Robert_B.wav'
    sound_info = upload_sound(file_name)
    create_sound_distortion_filter(sound_info, file_name)
