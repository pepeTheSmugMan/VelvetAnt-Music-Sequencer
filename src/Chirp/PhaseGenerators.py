import numpy as np
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

class PhaseGenerator(ABC):

    @abstractmethod
    def create_phase(self, t, frequency):
        pass


class LinearPhaseGenerator(PhaseGenerator):

    def create_phase(self, t: np.ndarray, frequency: float) -> np.ndarray:
        return 2 * np.pi * frequency * t


class DialPhaseGenerator(PhaseGenerator):

    def __init__(self, interval: int, frequencyDrop: int, sample_rate_source):
        self.interval = interval
        self.frequencyDrop = frequencyDrop
        self.sample_rate_source = sample_rate_source # so we can manipulate sample_rate from just one place, the Instrument

    def create_phase(self, t: np.ndarray, frequency: float) -> np.ndarray:

        interval = self.sample_rate_source.sample_rate/self.interval
        speed = np.where(
            (np.arange(len(t)) // interval ) % 2 == 0,
            frequency, 
            frequency-self.frequencyDrop
        )
        return 2 * np.pi * np.cumsum(np.diff(t, prepend=0) * speed)