import numpy as np


# Example simple system: Linear time-invariant system
# y(t) = k * x(t)  (gain system)
def linear_system(x, k=1.0):
    return k * x


# Example: simple first-order system
# y(t) = x(t) + 0.5*x(t-1)  (discrete approximation)
def discrete_system(x, alpha=0.5):
    y = np.zeros_like(x)
    y[0] = x[0]
    for i in range(1, len(x)):
        y[i] = x[i] + alpha * x[i - 1]
    return y
