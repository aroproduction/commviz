import numpy as np


def time_axis(t_min=-1, t_max=1, num=1000):
    return np.linspace(t_min, t_max, num)


def unit_impulse(t):
    return np.where(np.isclose(t, 0), 1.0, 0.0)


def unit_step(t):
    return np.where(t >= 0, 1.0, 0.0)


def ramp(t):
    return np.where(t >= 0, t, 0.0)


def exponential(t, a=1.0):
    return np.exp(a * t) * (t >= 0)


def sinusoid(t, amplitude=1.0, frequency=1.0, phase=0.0):
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)


def time_axis(t_min, t_max):
    duration = abs(t_max - t_min)

    if duration <= 1:
        num = 1000
    elif duration <= 10:
        num = 2000
    elif duration <= 100:
        num = 5000
    else:
        num = 10000  # cap for performance

    return np.linspace(t_min, t_max, num)
