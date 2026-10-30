import sounddevice  # Sound card communication
import Chirp        # Synthesizer
import Antennae     # Sequencer
import Chrysalis    # Mixer
import numpy as np

if __name__ == "__main__":

    Chirp.Presets.square.volume = 0.25
    Chrysalis.Mixer.speed = 1.0
    song = Chrysalis.Mixer.segment_to_melody(Chirp.Presets.ASDRdialSine, Antennae.SongExamples.megalovania)

    # instrument presentation
    sounddevice.play(song)
    sounddevice.wait()
