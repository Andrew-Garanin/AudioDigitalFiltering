import copy
import math
from datetime import datetime

import numpy as np

from Sound import Sound


def create_sound_distortion_filter(sound: Sound, blend_value, drive_value, range_value, volume_value):
    filtered_sound = copy.deepcopy(sound)
    # blend = 2
    # drive = 5
    # range1 = 5
    # volume = 10
    for i, value in enumerate(filtered_sound.wav_data):
        # if i % 2 == 0:
        filtered_sound.wav_data[i] = (((((2 / math.pi) * math.atan(
            filtered_sound.wav_data[i] * drive_value * range_value)) * blend_value) + (
                filtered_sound.wav_data[i] * (1 - blend_value))) / 2) * volume_value
    filtered_sound.filter_name = 'Distortion'
    print('Звук создан')
    return filtered_sound


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
    initial_time = datetime.now()

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
    print('time', datetime.now() - initial_time)
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