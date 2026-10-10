import sounddevice
import Chirp
import numpy as np

if __name__ == "__main__":

    sounddevice.default.samplerate = Chirp.Instrument.sample_rate

    # instrument presentation
    sounddevice.play(Chirp.Presets.sine.create_tone(1.0, Chirp.pianoScale["4C"], volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.triangle.create_tone(1.0, Chirp.pianoScale["4C"], volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.square.create_tone(1.0, Chirp.pianoScale["5C"], volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.sawtoooth.create_tone(1.0, Chirp.pianoScale["4G"], volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.tangent.create_tone(1.0, Chirp.pianoScale["3G"], volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.silence.create_tone(1.0))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.tangent.create_dial_tone(1.0, 440, 360, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.sawtoooth.create_dial_tone(1.0, 440, 360, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.square.create_dial_tone(1.0, 440, 360, volume=0.2, interval=50))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.sine.create_dial_tone(1.0, 440, 360, volume=0.2, interval=10))
    sounddevice.wait()

    #noies (percussion) presentation
    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 1, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 5, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 10, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 25, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 50, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 75, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 100, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 125, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 250, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 375, volume=0.2))
    sounddevice.wait()

    sounddevice.play(Chirp.Presets.noise.create_tone(1.0, 500, volume=0.2))
    sounddevice.wait()