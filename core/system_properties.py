import numpy as np


# ------------------------
# Linearity: output = a*system(x1) + b*system(x2)
def linearity_test(x1, x2, system_func, a=1, b=1):
    y1 = system_func(x1)
    y2 = system_func(x2)
    y_combined = system_func(a * x1 + b * x2)
    expected = a * y1 + b * y2
    return y_combined, expected


# ------------------------
# Time-invariance: y(t-t0) ?= system(x(t-t0))
def time_invariance_test(x, system_func, shift_idx):
    # shift input
    x_shifted = np.roll(x, shift_idx)
    y_original = system_func(x)
    y_shifted = system_func(x_shifted)
    y_expected = np.roll(y_original, shift_idx)
    return y_shifted, y_expected


# ------------------------
# Causality: output depends only on past
# Simulate by zeroing future input
def causality_test(x, system_func):
    x_future_blocked = x.copy()
    x_future_blocked[1:] = 0  # block future values
    y = system_func(x_future_blocked)
    return y


# ------------------------
# Stability: BIBO test (Bounded input)
def stability_test(x, system_func):
    y = system_func(x)
    is_stable = np.all(np.abs(y) < 1e6)  # arbitrary bound
    return y, is_stable
