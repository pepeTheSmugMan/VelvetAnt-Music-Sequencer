import numpy as np
from scipy import signal
from .Instruments import *
from matplotlib import pyplot as plt

#simple tones
sine = SimpleTone(np.sin)
tangent = SimpleTone(np.tan)
square = SimpleTone(signal.square)

#dial tones
dialSine = DialTone(np.sin, 40, 60)

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

#! damn this is cursed as hell 😂 get rid of this goofy thing later
ASDRdialSine = ADSRSynth(np.sin, 0.1, 0.1, 0.7, 0.5, 1.0)
helperDial = DialTone(lambda a: a, 10, 20)
ASDRdialSine._create_phase = helperDial._create_phase

ASDRbasicSine = ADSRSynth(np.sin, 0.0, 0.0, 1.0, 0.0, 1.0) # same as sine