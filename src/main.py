import sounddevice  # Sound card communication
import Chirp        # Synthesizer
import Antennae     # Sequencer
import Chrysalis    # Mixer
import numpy as np

if __name__ == "__main__":

    Chirp.Presets.square.volume = 0.25
    print(Chirp.Presets.square.volume)
    song = Chrysalis.Mixer.create_track(Chirp.Presets.square, Antennae.song, Chirp.pianoScale)

    # instrument presentation
    sounddevice.play(song)
    sounddevice.wait()
