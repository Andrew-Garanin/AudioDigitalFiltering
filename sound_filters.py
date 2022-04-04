import copy
import math
from datetime import datetime

import numpy as np

from Sound import Sound


# DONE!
def create_sound_distortion_filter(sound: Sound, blend_value, drive_value, range_value, volume_value):
    filtered_sound = copy.deepcopy(sound)

    clipping_point = 32768

    for i, value in enumerate(filtered_sound.wav_data):
        clear_sample = copy.deepcopy(filtered_sound.wav_data[i])
        filtered_sound.wav_data[i] = (((((2. / math.pi) * math.atan(
            clear_sample * drive_value * range_value / clipping_point) * clipping_point) * blend_value) + (
                                               clear_sample * (1. - blend_value)))) * volume_value
    filtered_sound.filter_name = 'Distortion'
    print('Звук создан')
    return filtered_sound


# DONE!
def create_speed_up(sound: Sound, factor_length):
    """
    Speed up audio stream by deleting samples from array
    :param sound: sound which we need transform
    :param factor_length: percentage for final length of audio depends on original one
    :return: speed up filtered Sound
    """
    filtered_sound = copy.deepcopy(sound)
    temp = np.array(filtered_sound.wav_data)

    original_len = len(temp)
    new_len = original_len * factor_length
    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (original_len / (original_len - new_len)) * filtered_sound.channels
    i = len(filtered_sound.wav_data) - 1
    while i > 2:
        floored_index = math.floor(i)
        temp = np.delete(temp, floored_index)
        temp = np.delete(temp, floored_index - 1)

        i -= step_length

    filtered_sound.wav_data = temp
    return filtered_sound


# DONE!
def create_slow_down(sound: Sound, factor_length):
    """
    Slow down audio stream by adding samples to array
    :param sound: sound which we need transform
    :param factor_length: percentage for final length of audio depends on original one
    :return: slowed down filtered Sound
    """
    filtered_sound = copy.deepcopy(sound)

    original_len = len(filtered_sound.wav_data)
    new_len = math.floor(original_len * factor_length)

    temp = np.array(filtered_sound.wav_data)

    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (original_len / (new_len - original_len)) * filtered_sound.channels
    print('step_length', step_length)
    i = len(filtered_sound.wav_data) - 1
    while i > 4:
        floored_index = math.floor(i)
        value1 = temp[floored_index]
        floored_index -= 1
        value2 = temp[floored_index]

        temp = np.insert(temp, floored_index, value1)
        temp = np.insert(temp, floored_index, value2)
        i -= step_length

    filtered_sound.wav_data = temp
    print('Sound created!')
    return filtered_sound


# DONE!
def create_sound_echo_filter(sound: Sound, delay_time_value, echo_level_value, blur_interval_value):
    filtered_sound = copy.deepcopy(sound)
    sub_frame_rate = sound.frame_rate / sound.channels

    # blur_offset = math.floor(sub_frame_rate / 1000 * blur_interval_value)
    blur_offset = 2 * blur_interval_value

    time_delay = math.floor(sub_frame_rate * delay_time_value)  # пол секунды  * delay time

    for i, value in enumerate(filtered_sound.first_channel):
        if i + time_delay < len(sound.first_channel):
            avarage = np.float((np.float(sound.first_channel[i]) + np.float(sound.first_channel[i - blur_offset]) +
                                np.float(sound.first_channel[i + blur_offset]) + np.float(
                        sound.first_channel[i - (blur_offset * 2)]) +
                                np.float(sound.first_channel[i + (blur_offset * 2)])) / 5)
            filtered_sound.first_channel[i + time_delay] += avarage * echo_level_value

    for i, value in enumerate(filtered_sound.second_channel):
        if i + time_delay < len(sound.second_channel):
            avarage = np.float((np.float(sound.second_channel[i]) + np.float(sound.second_channel[i - blur_offset]) +
                                 np.float(sound.second_channel[i + blur_offset]) + np.float(
                        sound.second_channel[i - (blur_offset * 2)]) +
                                 np.float(sound.second_channel[i + (blur_offset * 2)])) / 5)
            filtered_sound.second_channel[i + time_delay] += avarage * echo_level_value

    filtered_sound.filter_name = 'Echo'
    print('Звук создан')
    return filtered_sound


# DONE!
def create_sound_pop_click_remove_filter(sound: Sound, sensitivity_value, fade_length_value, mute_power_value):
    filtered_sound = copy.deepcopy(sound)

    fade_length = fade_length_value
    fade_out_length = math.floor(fade_length / 5)

    fade_in = np.arange(0., 1., 1 / fade_length) ** mute_power_value
    fade_out = np.arange(1., 0., -1 / fade_out_length)  # Не хотим, чтобы звук помер

    for i, sample in enumerate(filtered_sound.wav_data):
        if i + 1 < len(filtered_sound.wav_data) and math.fabs(
                filtered_sound.wav_data[i] - filtered_sound.wav_data[i + 1]) > sensitivity_value:
            problem_sample = i
            print(i)

            filtered_sound.wav_data[(problem_sample - fade_out_length):(problem_sample)] = np.multiply(
                filtered_sound.wav_data[(problem_sample - fade_out_length):(problem_sample)], fade_out)

            filtered_sound.wav_data[problem_sample:(problem_sample + fade_length)] = np.multiply(
                filtered_sound.wav_data[problem_sample:(problem_sample + fade_length)], fade_in)
    print('Звук создан')
    return filtered_sound


# https://www.desmos.com/calculator/ebdtbxgbq0?lang=ru
def fade_in_fade_out(sound: Sound, in_len, start_mute_power_value, out_len, end_mute_power_value):
    """
    Add a smooth fade in and fade out for audio
    :param sound: sound which we need transform
    :param in_len: length in samples to fade on start
    :param start_mute_power_value: power of fade for start
    :param out_len: length in samples to fade on end
    :param end_mute_power_value: power of fade for end
    :return: filtered audio with fades
    """
    filtered_sound = copy.deepcopy(sound)
    # generates a fades and powered by (1 / mute_power)
    fade_in = np.arange(0., 1., 1 / in_len) ** (1 / start_mute_power_value)
    fade_out = np.arange(1., 0., -1 / out_len) ** (1 / end_mute_power_value)

    # multiply slice of array by fade in array and gets a smooth increase volume
    filtered_sound.wav_data[:in_len] = np.multiply(filtered_sound.wav_data[:in_len], fade_in)
    # same for fade out
    filtered_sound.wav_data[-out_len:] = np.multiply(filtered_sound.wav_data[-out_len:], fade_out)

    return filtered_sound


def create_remove_silence_filter(sound: Sound, offset_samples, aggression):
    """
    Removing a silence from audio
    :param sound:  sound which we need transform
    :param offset_samples: offset param for better transition between silence drops
    :param aggression: how aggressively we need to search a silence fragments
    :return: filtered audio without silence
    """
    filtered_sound = copy.deepcopy(sound)
    start_pos = 0
    wav_data_copy = np.copy(filtered_sound.wav_data)

    # run through array and looking for silens segments by compare value of sample
    # with aggression param.
    for i, sample in enumerate(wav_data_copy):
        if math.fabs(sample) < aggression and start_pos == 0:
            start_pos = i

        if math.fabs(sample) > aggression and start_pos != 0:
            end_pos = i

            if end_pos - start_pos < offset_samples * 3:
                start_pos = 0
                continue

            # For better transition apply an offset_samples
            start_pos += math.floor(offset_samples / 2)
            end_pos -= math.floor(offset_samples / 2)
            # 'cause changing a size of array, we need to shift indexes by diff of original one size
            end_pos -= len(wav_data_copy) - len(filtered_sound.wav_data)
            start_pos -= len(wav_data_copy) - len(filtered_sound.wav_data)

            # Slices it and merge again
            first_part = filtered_sound.wav_data[:start_pos]
            second_part = filtered_sound.wav_data[end_pos:]
            filtered_sound.wav_data = np.concatenate((first_part, second_part))

            # reset a start position
            start_pos = 0

    return filtered_sound
