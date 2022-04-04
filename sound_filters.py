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
    filtered_sound = copy.deepcopy(sound)
    temp = np.array(filtered_sound.wav_data)

    print(len(temp))
    # factor_length - is a percentage of original size to some value. example 75% (been 20 samples -> will be 15)
    # factor_length = 0.8
    # original_len / original_len-new_len = step_length
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
    print('final factor_length: ', len(temp) / original_len)
    print('final len: ', len(temp))
    filtered_sound.wav_data = temp
    print('Sound created!')
    return filtered_sound


# DONE!
def create_slow_down(sound: Sound, factor_length):
    initial_time = datetime.now()
    filtered_sound = copy.deepcopy(sound)
    # factor_length - is a percentage of original size to some value. example 130% (been 20 samples -> will be 26)
    # factor_length = 2

    original_len = len(filtered_sound.wav_data)
    new_len = math.floor(original_len * factor_length)

    temp = np.array(filtered_sound.wav_data)

    # multiply on channels width 'couse we need to del a frame, not a single sample!
    step_length = (original_len / (new_len - original_len)) * filtered_sound.channels
    print('step_length', step_length)
    i = len(filtered_sound.wav_data) - 1
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

    filtered_sound.wav_data = temp
    print('time', datetime.now() - initial_time)
    print('final factor_length: ', len(temp) / original_len)
    print('final len: ', len(temp))
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
            avarage = (sound.first_channel[i] + sound.first_channel[i - blur_offset] + sound.first_channel[
                i + blur_offset] + sound.first_channel[i - (blur_offset * 2)] + sound.first_channel[
                           i + (blur_offset * 2)]) / 5
            filtered_sound.first_channel[i + time_delay] += avarage * echo_level_value

    for i, value in enumerate(filtered_sound.second_channel):
        if i + time_delay < len(sound.second_channel):
            avarage = (sound.first_channel[i] + sound.first_channel[i - blur_offset] + sound.first_channel[
                i + blur_offset] + sound.first_channel[i - (blur_offset * 2)] + sound.first_channel[
                           i + (blur_offset * 2)]) / 5
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


def fade_in_fade_out(sound: Sound, start_n_samples, end_n_samples, mute_power_value):
    filtered_sound = copy.deepcopy(sound)

    fade_in_length = start_n_samples
    fade_out_length = end_n_samples

    fade_in = np.arange(0., 1., 1 / fade_in_length) ** mute_power_value
    fade_out = np.arange(1., 0., -1 / fade_out_length) ** mute_power_value

    for i, sample in enumerate(filtered_sound.wav_data):
        # if i + 1 < len(filtered_sound.wav_data) and math.fabs(filtered_sound.wav_data[i] - filtered_sound.wav_data[i + 1]) > sensitivity_value:
        #     problem_sample = i
        #     print(i)

            filtered_sound.wav_data[0:fade_in_length] = np.multiply(filtered_sound.wav_data[0:fade_in_length], fade_in)

            filtered_sound.wav_data[(len(filtered_sound.wav_data)-fade_out_length):] = np.multiply(filtered_sound.wav_data[(len(filtered_sound.wav_data)-fade_out_length):], fade_in)
    print('Звук создан')
    return filtered_sound



def create_remove_silence_filter(sound: Sound, offset_samples, aggression):
    filtered_sound = copy.deepcopy(sound)

    start_pos = 0

    print('original len: ', len(filtered_sound.wav_data))
    wav_data_copy = np.copy(filtered_sound.wav_data)
    for i, sample in enumerate(wav_data_copy):
        # TODO: set an aggression param
        if math.fabs(sample) < aggression and start_pos == 0:
            start_pos = i

        if math.fabs(sample) > aggression and start_pos != 0:
            end_pos = i

            if end_pos - start_pos < offset_samples * 3:
                start_pos = 0
                continue

            print('start: ', start_pos, "time: ", round(start_pos / filtered_sound.frame_rate / 2, 2))
            print('end: ', end_pos, "time: ", round(end_pos / filtered_sound.frame_rate / 2, 2))
            # For better transition apply an offset_samples
            start_pos += math.floor(offset_samples / 2)
            end_pos -= math.floor(offset_samples / 2)
            print("len(filtered_sound.wav_data)", len(filtered_sound.wav_data))
            end_pos -= len(wav_data_copy) - len(filtered_sound.wav_data)
            start_pos -= len(wav_data_copy) - len(filtered_sound.wav_data)
            print('after start: ', start_pos, "time: ", round(start_pos / filtered_sound.frame_rate / 2, 2))
            print('after end: ', end_pos, "time: ", round(end_pos / filtered_sound.frame_rate / 2, 2))

            first_part = filtered_sound.wav_data[:start_pos]
            second_part = filtered_sound.wav_data[end_pos:]

            filtered_sound.wav_data = np.concatenate((first_part, second_part))

            start_pos = 0

    print('final len: ', len(filtered_sound.wav_data))

    print('Звук создан')
    return filtered_sound
