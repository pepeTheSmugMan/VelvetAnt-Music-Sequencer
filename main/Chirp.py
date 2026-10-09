import numpy as np
from scipy import signal
import sounddevice

class Chirp:

    def __init__(self, sample_rate=48_000):
        
        self.sample_rate = sample_rate
        np.random.seed = 42
        

    def create_tone(self, instrument: callable, duration: float, frequency: float, volume: float =1.0, type="constant", repeat: int=1):

        t = np.arange(self.sample_rate * duration) / self.sample_rate

        if type == "constant":
            phase = 2 * np.pi * frequency * t

        elif type == "dialtone":
            interval = self.sample_rate/20
            speed = np.where(
                (np.arange(len(t)) // interval ) % 2 == 0,
                frequency, 
                frequency-200
            )
            phase = 2 * np.pi * np.cumsum(np.diff(t, prepend=0) * speed)

        
        tone = instrument(phase)
        tone = volume * np.clip(tone, -1, 1)
        tone = np.repeat(tone, repeat)[:int(self.sample_rate * duration)]

        return tone


if __name__ == "__main__":
    chirp = Chirp()
    
    sounddevice.play(
        chirp.create_tone(
            instrument=np.tan,
            duration=1.0,
            frequency=440.0,
            type="dialtone"
        ),
        48000
    )
    sounddevice.wait()