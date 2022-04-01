# import time
# import math
# import pyaudio
# from cffi.backend_ctypes import xrange
#
#
# class Beeper(object):
#
#     def __init__(self, **kwargs):
#         self.bitrate = kwargs.pop('bitrate', 16000)
#         self.channels = kwargs.pop('channels', 1)
#         self._p = pyaudio.PyAudio()
#         self.stream = self._p.open(
#             format = self._p.get_format_from_width(1),
#             channels = self.channels,
#             rate = self.bitrate,
#             output = True,
#         )
#         self._queue = []
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.stream.stop_stream()
#         self.stream.close()
#
#     def tone(self, frequency, length=1000, play=False, **kwargs):
#
#         number_of_frames = int(self.bitrate * length / 1000.)
#
#         record = False
#         x = 0
#         y = 0
#         while 1:
#             x += 1
#             v = math.sin(x / ((self.bitrate / float(frequency)) / math.pi))
#
#             # Find where the sin tip starts.
#             if round(v, 3) == +1:
#                 record = True
#
#             if record:
#                 self._queue.append(chr(int(v * 127 + 128)))
#                 y += 1
#                 if y > number_of_frames and round(v, 3) == +1:
#                     # Always end on the high tip of the sin wave to clips align.
#                     break
#
#     def play(self):
#         sound = ''.join(self._queue)
#         self.stream.write(sound)
#         time.sleep(0.1)
#
#
# with Beeper(bitrate=88000, channels=2) as beeper:
#     i = 0
#     for f in xrange(1000, 800-1, int(round(-25/2.))):
#         i += 1
#         length = math.log(i + 1) * 250 / 2. / 2.
#         beeper.tone(frequency=f, length=int(length))
#     beeper.play()

import numpy
import pyaudio
import math
import random


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    waveform = numpy.sin(numpy.arange(length) * factor)
    return waveform


def play_tone(stream, frequency, length, rate=44100):
    chunks = [sine(frequency, length, rate)]

    chunk = numpy.concatenate(chunks) * 0.25

    fade = 200

    fade_in = numpy.arange(0., 1., 1 / fade)
    fade_out = numpy.arange(1., 0., -1 / fade)

    chunk[:fade] = numpy.multiply(chunk[:fade], fade_in)
    chunk[-fade:] = numpy.multiply(chunk[-fade:], fade_out)

    stream.write(chunk.astype(numpy.float32).tostring())


def bassline():
        frequency = 300
        for i in range(1000000):
            play_tone(stream, frequency, .15)
            change = random.choice([-75, -75, -10, 10, 2, 3, 100, -125])
            print (frequency)
            if frequency < 0:
                frequency = random.choice([100, 200, 250, 300])
            else:
                frequency = frequency + change

if __name__ == '__main__':
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=4)

bassline()