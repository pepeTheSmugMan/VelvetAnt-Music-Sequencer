import numpy as np
from scipy import signal
from .Instruments import SimpleTone, Noise, Sawtooth, Silence

sine = SimpleTone(np.sin)
tangent = SimpleTone(np.tan)
square = SimpleTone(signal.square)
triangle = Sawtooth(0.5)
sawtoooth = Sawtooth(1.0)
noise = Noise()
silence = Silence()