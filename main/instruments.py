

instruments = {
    "noise" : np.random.rand,
    "sine" : np.sin,
    "tangent" : np.tan,
    "square": signal.square,
    "sawtooth": signal.sawtooth 
}

# what has to be known to play a sound:
# FUNCTION
# PHASE
# FUNCTION PARAMETERS (e.g. sawtooth width)
# DURATION
# VOLUME
# (optional) REPEAT


#! constant
# phase = 2 * np.pi * frequency * t * repeat

#! dialtone
# interval = (self.sample_rate/20)/repeat
# speed = np.where(
#     (np.arange(len(t)) // interval ) % 2 == 0,
#     frequency, 
#     frequency-50
# )
# phase = 2 * np.pi * np.cumsum(np.diff(t, prepend=0) * speed) * repeat

#! noise
# phase = int(self.sample_rate * duration)