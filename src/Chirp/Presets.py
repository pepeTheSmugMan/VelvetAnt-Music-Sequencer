import numpy as np
from scipy import signal
from .Instruments import *
from .PhaseGenerators import *
from matplotlib import pyplot as plt

#simple tones
sine = SimpleTone(np.sin)
tangent = SimpleTone(np.tan)
square = SimpleTone(signal.square)

#dial tones
dialSine = SimpleTone(np.sin, DialPhaseGenerator(40, 60, Instrument))

#saws
sawtoooth = SimpleTone(lambda phase : signal.sawtooth(phase, 1.0))
saw_sandwasp = SimpleTone(lambda phase : signal.sawtooth(phase, 0.95))
saw_wasp = SimpleTone(lambda phase : signal.sawtooth(phase, 0.9))
saw_fly = SimpleTone(lambda phase : signal.sawtooth(phase, 0.8))
saw_hornet = SimpleTone(lambda phase : signal.sawtooth(phase, 0.7))
saw_bumblebee = SimpleTone(lambda phase : signal.sawtooth(phase, 0.6))
triangle = SimpleTone(lambda phase : signal.sawtooth(phase, 0.5))

#other
noise = Noise()
silence = Silence()

#ADSR
ADSRsine = ADSRSynth(np.sin, 0.1, 0.1, 0.7, 0.5, 1.0)

ADSRdialSine = ADSRSynth(
    tone_function= np.sin,
    attack=0.1,
    decay=0.1,
    sustain=0.7,
    release=0.5,
    peak=1.0,
    phase_generator=DialPhaseGenerator(10, 20, Instrument)
)

ADSRbasicSine = ADSRSynth(np.sin) # same as sine