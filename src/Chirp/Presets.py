import numpy as np
from scipy import signal
from .Instruments import SimpleTone, Noise, Sawtooth, Silence

#simple tones
sine = SimpleTone(np.sin)
tangent = SimpleTone(np.tan)
square = SimpleTone(signal.square)

#saws
sawtoooth = Sawtooth(1.0)
saw_sandwasp = Sawtooth(0.95)
saw_wasp = Sawtooth(0.9)
saw_fly = Sawtooth(0.8)
saw_hornet = Sawtooth(0.7)
saw_bumblebee = Sawtooth(0.6)
triangle = Sawtooth(0.5)

#other
noise = Noise()
silence = Silence()