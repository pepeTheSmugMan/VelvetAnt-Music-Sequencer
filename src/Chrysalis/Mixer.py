import numpy as np

class Mixer:

    speed = 1.0

    @staticmethod
    def segment_to_melody(instrument, segment):
        return instrument.create_melody(segment, Mixer.speed)

    @staticmethod
    def track_to_melody():
        pass

    @staticmethod
    def bind_tracks():
        pass



