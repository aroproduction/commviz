import numpy as np


class Signal:
    """Core Signal Class"""

    def __init__(self, func, name, formula, params=None):
        self.func = func
        self.name = name
        self.formula = formula
        self.params = params or {}

    def evaluate(self, t):
        return self.func(t, **self.params)

    # -------- Algebra --------
    def __add__(self, other):
        return Signal(
            lambda t: self.evaluate(t) + other.evaluate(t),
            name=f"({self.name}+{other.name})",
            formula=f"{self.formula} + {other.formula}",
        )

    def __mul__(self, other):
        return Signal(
            lambda t: self.evaluate(t) * other.evaluate(t),
            name=f"({self.name}*{other.name})",
            formula=f"{self.formula} · {other.formula}",
        )

    # -------- Transforms --------
    def shift(self, tau):
        return Signal(
            lambda t: self.evaluate(t - tau),
            name=f"{self.name}(t-{tau})",
            formula=f"{self.formula.replace('t', f'(t-{tau})')}",
        )

    def scale(self, k):
        return Signal(
            lambda t: k * self.evaluate(t),
            name=f"{k}{self.name}",
            formula=f"{k}·({self.formula})",
        )

    def time_scale(self, a):
        """Time scaling: x(at)"""
        return Signal(
            lambda t: self.evaluate(a * t),
            name=f"{self.name}({a}t)",
            formula=f"{self.formula.replace('t', f'({a}t)')}",
        )


# Signal Factory Functions
# -----------------------------------------------------------------------


def unit_impulse():
    return Signal(
        func=lambda t: np.where(np.isclose(t, 0), 1.0, 0.0),
        name="Unit Impulse",
        formula="δ(t)",
    )


def unit_step(constant=1.0):
    return Signal(
        func=lambda t, constant=constant: np.where(t >= 0, constant, 0.0),
        name="Unit Step",
        formula="u(t)",
        params={"constant": constant},
    )


def ramp():
    return Signal(
        func=lambda t: np.where(t >= 0, t, 0.0),
        name="Ramp",
        formula="t × u(t)",
    )


def exponential(a=1.0):
    return Signal(
        func=lambda t, a=a: np.exp(a * t) * (t >= 0),
        name="Exponential",
        formula=f"e^({a}t)×u(t)",
        params={"a": a},
    )


def sinusoid(amplitude=1.0, frequency=1.0, phase=0.0):
    return Signal(
        func=lambda t, amplitude=amplitude, frequency=frequency, phase=phase: amplitude
        * np.sin(2 * np.pi * frequency * t + phase),
        name="Sinusoid",
        formula=f"{amplitude}·sin(2π{frequency}t+{phase})",
        params={
            "amplitude": amplitude,
            "frequency": frequency,
            "phase": phase,
        },
    )


def sinc_signal(amplitude=1.0):
    return Signal(
        func=lambda t, amplitude=amplitude: amplitude * np.sinc(t),
        name="Sinc",
        formula="sin(πt)/(πt)",
        params={"amplitude": amplitude},
    )


def signum_signal():
    return Signal(
        func=lambda t: np.sign(t),
        name="Signum",
        formula="sgn(t)",
    )


def rectangular_pulse(start=-1.0, end=1.0, amplitude=1.0):
    return Signal(
        func=lambda t, start=start, end=end, amplitude=amplitude: np.where(
            (t >= start) & (t <= end), amplitude, 0.0
        ),
        name="Rectangular Pulse",
        formula=f"{amplitude}·rect(t) , [{start},{end}]",
        params={"start": start, "end": end, "amplitude": amplitude},
    )


def triangular_wave(start=0.0, end=1.0, amplitude=1.0):
    def tri(t, start=start, end=end, amplitude=amplitude):
        x = 1 - np.abs(2 * (t - start) / (end - start) - 1)
        x[x < 0] = 0
        return amplitude * x

    return Signal(
        func=tri,
        name="Triangular",
        formula=f"tri(t) , [{start},{end}]",
        params={"start": start, "end": end, "amplitude": amplitude},
    )


# Registry
# ==============================
SIGNAL_REGISTRY = {
    "unit_impulse": unit_impulse,
    "unit_step": unit_step,
    "ramp": ramp,
    "exponential": exponential,
    "Sinusoidal": sinusoid,
    "sinc": sinc_signal,
    "signum": signum_signal,
    "rectangular": rectangular_pulse,
    "triangular": triangular_wave,
}


def get_available_signals():
    """Return all registered signal names in display format (title case with spaces)"""
    display_names = []
    for key in SIGNAL_REGISTRY.keys():
        # Replace underscores with space and capitalize each word
        name = key.replace("_", " ").title()
        display_names.append(name)
    return display_names


def get_signal_modes():
    return ("Continuous", "Discrete")
