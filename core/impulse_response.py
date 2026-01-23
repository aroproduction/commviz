import numpy as np

def impulse_response_linear(length=101):
    """Simple delta-like impulse response for linear system"""
    h = np.zeros(length)
    h[length // 2] = 1  # delta at center
    return h

def impulse_response_exponential(length=101, alpha=0.5):
    """Exponential decaying impulse response"""
    n = np.arange(length)
    h = (alpha ** n) * (n >= 0)
    return h

def impulse_response_ramp(length=101):
    """Ramp impulse response"""
    n = np.arange(length)
    h = n / np.max(n)
    return h
