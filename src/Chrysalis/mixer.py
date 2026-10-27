import numpy as np
from matplotlib import pyplot as plt

class Mixer:

    speed = 1.0

    @staticmethod
    def create_track(instrument, notes, scale):

        segment_duration = notes[0][1] * Mixer.speed
        sample_rate = instrument.sample_rate

        track = np.zeros(int(sample_rate * segment_duration))

        for note in notes[1]:

            startTime = note[0] * Mixer.speed
            duration = note[1] * Mixer.speed
            noteKey = note[2]

            sound = instrument.create_tone(duration, scale[noteKey])
            index = int(sample_rate * startTime)

            # print(track, index, sound)
            # print(len(track), len(sound))
            plt.plot

            track[index:(index+len(sound))] += sound
        
        return np.clip(track, -1, 1)

    @staticmethod
    def bind_tracks():
        pass



