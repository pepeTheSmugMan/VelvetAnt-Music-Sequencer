import numpy as np
from scipy import signal
import sounddevice
from abc import ABC, abstractmethod


class Instrument(ABC):

    sample_rate = 48000

    @abstractmethod
    def create_tone(self):
        pass

    @abstractmethod
    def create_phase(self):
        pass

    @staticmethod
    def create_t(sample_rate, duration):
        return np.arange(sample_rate * duration) / sample_rate

    @staticmethod
    def normalise(tone, volume):
        return volume * np.clip(tone, -1, 1)


class SimpleTone(Instrument):

    def __init__(self, tone_function:callable):
        self.tone_function = tone_function
    
    def create_phase(self, t, frequency):
        return 2 * np.pi * frequency * t

    def create_dialtone_phase(self, t, frequencyHigh, frequencyLow, interval):
        interval = Instrument.sample_rate/interval
        speed = np.where(
            (np.arange(len(t)) // interval ) % 2 == 0,
            frequencyHigh, 
            frequencyLow
        )
        return 2 * np.pi * np.cumsum(np.diff(t, prepend=0) * speed)

    def _create_tone_from_phase(self, phase, volume):
        tone = self.tone_function(phase)
        return self.normalise(tone, volume)


    def create_tone(self, duration, frequency, volume=1.0):
        t = self.create_t(Instrument.sample_rate, duration)
        phase = self.create_phase(t, frequency)
        return self._create_tone_from_phase(phase, volume)

    def create_dial_tone(self, duration, frequencyHigh, frequencyLow, volume=1.0, interval=20):
        t = self.create_t(Instrument.sample_rate, duration)
        phase = self.create_dialtone_phase(t, frequencyHigh, frequencyLow, interval)
        return self._create_tone_from_phase(phase, volume)
    

class Sawtooth(SimpleTone):

    def __init__(self, width=0.5):
        self.width = width
    
    def tone_function(self, phase):
        return signal.sawtooth(phase, self.width)

    
class Noise(Instrument):

    def create_phase(self, t, duration):
        return np.random.rand(int(Instrument.sample_rate*duration))
    
    def create_tone(self, duration, repeat=1, volume=1.0):
        t = self.create_t(Instrument.sample_rate, duration)
        phase = self.create_phase(t, duration)
        tone = np.repeat(phase, repeat)[:int(Instrument.sample_rate * duration)]
        return self.normalise(tone, volume)


if __name__ == "__main__":
    
    sounddevice.default.samplerate = Instrument.sample_rate

    sine = SimpleTone(np.sin)
    square = SimpleTone(np.square)
    tangent = SimpleTone(np.tan)
    sawtooth = Sawtooth()
    noise = Noise()

    sounddevice.play(
        sawtooth.create_tone(1.0, 440, volume=0.2) 
    )
    sounddevice.wait()

    sounddevice.play(
        sawtooth.create_dial_tone(1.0, 440, 400, volume=0.2)
    )
    sounddevice.wait()

    sounddevice.play(
        noise.create_tone(1.0, repeat=50, volume=0.2)
    )
    sounddevice.wait()