import sounddevice
import Chirp
import numpy as np


if __name__ == "__main__":
    
    sounddevice.default.samplerate = Chirp.Instrument.sample_rate

    sine = Chirp.SimpleTone(np.sin)
    square = Chirp.SimpleTone(np.square)
    tangent = Chirp.SimpleTone(np.tan)
    sawtooth = Chirp.Sawtooth(1.0)
    noise = Chirp.Noise()

    duration = 0.3
    frequency = 440
    volume = 0.2

    sounddevice.play(
        sawtooth.create_tone(duration, frequency, volume=volume) 
    )
    sounddevice.wait()

    sounddevice.play(
        sawtooth.create_dial_tone(duration, frequency, frequency/2, interval=50, volume=volume)
    )
    sounddevice.wait()

    sounddevice.play(
        noise.create_tone(duration, repeat=50, volume=volume)
    )
    sounddevice.wait()