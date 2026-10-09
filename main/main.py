import numpy as np
import sounddevice as sd
from scipy import signal
import sys
from matplotlib import pyplot as plt

np.set_printoptions(threshold=128)
np.random.seed = 42


sample_rate = 48000
frequency = 440
duration = 1.0

zeroSample = np.zeros(int(sample_rate * duration))
t = np.arange(sample_rate * duration) / sample_rate

# # tangens
tg1 = np.tan(2 * np.pi * frequency * t)
tg2 = np.tan(2 * np.pi * frequency/2 * t)
#? tan = volume * np.clip(tan, -1, 1)

# sd.play(
#     np.concatenate([tg1, zeroSample, tg2, zeroSample, (tg1+tg2)/2, zeroSample]),
#     sample_rate
# )
# sd.wait()

# # sinus
# sin1 = np.sin(2 * np.pi * frequency * t)
# sin2 = np.sin(2 * np.pi * (frequency + frequency/8) * t)

# sd.play(
#     np.concatenate([sin1, zeroSample, sin2, zeroSample, (sin1+sin2)/2, zeroSample]),
#     sample_rate
# )
# sd.wait()

#!
def play(frequency, volume=1, repeat=1):

    sin = np.tan(2 * np.pi * frequency * t)
    sin = volume * np.clip(sin, -1, 1)
    #sin = np.repeat(sin, repeat)[:int(sample_rate*duration)] #+ frequency * repeat in first declaration

    plt.plot(sin[:500])
    plt.show()

    sd.play(
        np.concatenate([sin, zeroSample]),
        sample_rate
    )
    sd.wait()

for i in [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25]:
    play(i, 1)
for i in [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 523.25][::-1]:
    play(i)

#!
# def saw(frequency, volume=1, width=0.5):

#     saw = signal.sawtooth(2 * np.pi * frequency * t, width)
#     saw = volume * np.clip(saw, -1, 1)

#     sd.play(np.concatenate([saw, zeroSample]), sample_rate)
#     sd.wait()

# for i in range(11):
#     print(i)
#     saw(440, 1, i/10)
#     saw(440, 1, (10-i)/10)

#!
# def noise(volume=1, repeat=1):

#     noise = np.random.rand(int(sample_rate*duration))
#     noise = np.repeat(noise, repeat)[:int(sample_rate*duration)]
#     sd.play(np.concatenate([noise, zeroSample]), sample_rate)
#     sd.wait()

# for i in [20, 30, 40, 50]:
#     noise(1, i)



# # square
# sig = np.sin(2 * np.pi * t)
# square1 = signal.square(2 * np.pi * frequency * t)
# square2 = signal.square(2 * np.pi * frequency * t, duty=(sig + 1)/2)

# # sawtooth
# saw1 = signal.sawtooth(2 * np.pi * frequency * t, 1.0)
# saw2 = signal.sawtooth(2 * np.pi * frequency/2 * t, 0.5) # triangle
# saw3 = signal.sawtooth(2 * np.pi * frequency/2 * t, 0.0)
# sd.play(
#     np.concatenate([saw1, zeroSample, saw2, zeroSample, saw3, zeroSample, (saw1+saw2)/2, zeroSample]),
#     sample_rate
# )
# sd.wait()

# noise
# random = np.random.rand(int(sample_rate * duration))
# random = np.repeat(random, magical_number) # (from 1 to 1000 makes interesting stuff)
# sd.play(random, sample_rate)
# sd.wait()

# stereo
# sawStereo = np.column_stack((saw1, saw2))
# sinStereo = np.column_stack((sin1, sin2))
# tgStereo = np.column_stack((tg1, tg2))
# sd.play(
#     np.concatenate([stereoZeroSample, sawStereo, stereoZeroSample, sinStereo, stereoZeroSample, tgStereo]),
#     sample_rate
# )
# sd.wait()