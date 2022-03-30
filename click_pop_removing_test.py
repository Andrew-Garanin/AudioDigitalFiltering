import math
import ntpath
import os
import wave

import numpy
import numpy as np


if __name__ == '__main__':
    file_name = 'D:\\Projects\\PycharmProjects\\AudioDigitalFiltering\\input sounds\\plohoi_zvyk.wav'
    with wave.open(file_name,
                   'rb') as file:
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

    # p = pyaudio.PyAudio()
    # stream = p.open(format=pyaudio.paFloat32,
    #                 channels=2, rate=48000, output=1)

    fade = 10

    for i, sample in enumerate(sound_info['wav_data']):
        if i + 1 < len(sound_info['wav_data']) and math.fabs(sound_info['wav_data'][i] - sound_info['wav_data'][i + 1]) > 32500:
            fade_in = numpy.arange(0.2, 1., 0.8 / fade)
            fade_out = numpy.arange(1., 0.2, -0.8 / fade)
            problem_sample = i
            print(i)

            sound_info['wav_data'][(problem_sample - fade):(problem_sample)] = numpy.multiply(sound_info['wav_data'][(problem_sample - fade):(problem_sample)], fade_out)
            sound_info['wav_data'][problem_sample:(problem_sample + fade)] = numpy.multiply(sound_info['wav_data'][problem_sample:(problem_sample + fade)], fade_in)


    obj = wave.open(os.path.join('output sounds', 'distortion_' + ntpath.basename(file_name)), 'w')
    obj.setnchannels(sound_info['channels'])
    obj.setsampwidth(sound_info['sample_width'])
    obj.setframerate(sound_info['frame_rate'])
    obj.writeframes(sound_info['wav_data'].tobytes())
    obj.close()
