import numpy as np
from scipy import signal
import sounddevice
from abc import ABC, abstractmethod


class Instrument(ABC):

    sample_rate = 48000

    @staticmethod
    @abstractmethod
    def create_phase(self):
        pass

    @staticmethod
    @abstractmethod
    def create_tone(self):
        pass

    @staticmethod
    def create_t(sample_rate, duration):
        return np.arange(sample_rate * duration) / sample_rate

    @staticmethod
    def normalise(tone, volume):
        return volume * np.clip(tone, -1, 1)


class Sine(Instrument):
    
    def create_phase(t, frequency):
        return 2 * np.pi * frequency * t

    def create_tone(duration, frequency, volume=1.0):
        print(Sine.sample_rate)
        t = Sine.create_t(Sine.sample_rate, duration)
        phase = Sine.create_phase(t, frequency)
        tone = np.sin(phase)
        return Sine.normalise(tone, volume)


if __name__ == "__main__":
    
    sounddevice.play(
        Sine.create_tone(1.0, 440),
        Instrument.sample_rate
    )
    sounddevice.wait()