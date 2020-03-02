import numpy as np
import wpilib


class Piecewise:
    """https://0x0.st/-TSD"""
    
    def __init__(self, slow: float, fast: float):
        self.slow = slow
        self.fast = fast
        self.intersection = (1 - self.fast) / (self.slow - self.fast)

    def getValue(self, signal):
        sign = np.sign(signal)
        signal = abs(signal)
        if signal <= self.intersection:
            signal *= self.slow
        else:
            signal *= self.fast
            signal += (1-self.fast)
        return sign * signal

class Exponential:
    def __init__(self, exponent):
        self.exponent = exponent

    def getValue(self, signal):
        sign = np.sign(signal)
        signal **= self.exponent
        return sign * signal