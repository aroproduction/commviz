# Time shift
def time_shift(x, t, shift=0.0):
    t_shifted = t - shift
    return t_shifted, x  # return new time axis with same values


# Time scaling
def time_scale(x, t, scale=1.0):
    t_scaled = t / scale
    return t_scaled, x


# Time reversal
def time_reverse(x, t):
    t_rev = -t
    x_rev = x[::-1]  # flip values
    return t_rev, x_rev


# Amplitude scaling
def amplitude_scale(x, factor=1.0):
    return x * factor

