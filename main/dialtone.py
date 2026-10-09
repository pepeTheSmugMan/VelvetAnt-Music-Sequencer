import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd
from scipy import signal

sample_rate = 48000
frequency = 440.0
duration = 1.0

t = np.arange(sample_rate * duration) / sample_rate
interval = sample_rate/20

speed = np.where(
    (np.arange(len(t)) // interval ) % 2 == 0,
    frequency, 
    frequency-200
)

phase = 2 * np.pi * np.cumsum(np.diff(t, prepend=0) * speed)
tone = signal.sawtooth(phase, 0.5)

sd.play(tone, sample_rate)
sd.wait()