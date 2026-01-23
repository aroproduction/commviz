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


def time_axis(t_min, t_max, dt=None, num_points=1000):
    """
    Generate time axis from t_min to t_max.
    """
    if dt is not None:
        t = np.arange(t_min, t_max + dt, dt)
    else:
        t = np.linspace(t_min, t_max, num_points)
    return t
