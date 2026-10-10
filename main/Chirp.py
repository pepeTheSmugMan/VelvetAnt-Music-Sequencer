import numpy as np
from scipy import signal
import sounddevice

class Instrument:

    sample_rate = 48000

    def __init__(self, tone_function: callable, phase_function: callable):
        self.create_tone = tone_function
        self.create_phase = phase_function
        
    
    @staticmethod
    def create_t(sample_rate, duration):
        return np.arange(sample_rate * duration) / sample_rate

    @staticmethod
    def normalise(tone, volume):
        return volume * np.clip(tone, -1, 1)
    


def create_sine():

    def sine_create_tone(self, duration, frequency, volume=1.0):
        t = self.create_t(self.sample_rate, duration)
        phase = self.create_phase(t, frequency)
        tone = np.sin(phase)
        return self.normalise(tone, volume)

    return Instrument(
        phase_function = (
            lambda t, frequency :
            2 * np.pi * frequency * t
        ),
        tone_function = sine_create_tone
    )

if __name__ == "__main__":
    sine = create_sine()
    sounddevice.play(
        sine.create_tone(sine, 1.0, 440),
        sine.sample_rate
    )

    sounddevice.wait()

    # chirp = Chirp()
    # sounddevice.play(
    #     chirp.create_tone(
    #         instrument=np.random.rand,
    #         duration=1.0,
    #         frequency=220.0,
    #         volume=0.5,
    #         repeat=50,
    #         type="noise"
    #     ),
    #     48000
    # )
    


# class Chirp:

#     def __init__(self, sample_rate=48_000):
        
#         self.sample_rate = sample_rate
#         np.random.seed = 42
        

#     def create_tone(self, instrument: callable, duration: float, frequency: float, volume: float =1.0, type="constant", repeat: int=1):

#         t = np.arange(self.sample_rate * duration) / self.sample_rate

#         if type == "constant":
#             phase = 2 * np.pi * frequency * t * repeat

#         elif type == "dialtone":

#             interval = (self.sample_rate/50)/repeat
#             speed = np.where(
#                 (np.arange(len(t)) // interval ) % 2 == 0,
#                 frequency, 
#                 frequency-100
#             )
#             phase = 2 * np.pi * np.cumsum(np.diff(t, prepend=0) * speed) * repeat

#         elif type == "noise":
#             phase = int(self.sample_rate * duration)
            
        
#         tone = instrument(phase)
#         tone = volume * np.clip(tone, -1, 1)
#         tone = np.repeat(tone, repeat)[:int(self.sample_rate * duration)]

#         return tone