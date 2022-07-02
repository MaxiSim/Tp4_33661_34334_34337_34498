import math
import matplotlib.pyplot as plt
import numpy as np


class Modulator:

    def constant (t: float)->float:
        return 1

    def linear (t: float, t0: float)->float:
        return t/t0

    def invlinear (t: float, t0: float)->float:
        ans = 1-(t/t0)
        if ans < 0:
            return 0
        return ans

    def sin (a: float, t: float, f: float)->float:
        x = f*t
        return 1 + a * math.sin(x)

    def exp (t: float, t0: float)->float:
        x = 5*(t-t0)/t0
        return math.exp(x)

    def invexp (t: float, t0: float)->float:
        x = -5*t/t0
        return math.exp(x)

    def quartcos (t: float, t0: float)->float:
        x = (math.pi * t) / 2 * t0
        return math.cos(x)

    def quartsin (t: float, t0: float)->float:
        x = (math.pi * t) / 2 * t0
        return math.sin(x)

    def halfcos (t: float, t0: float)->float:
        x = (math.pi * t) / t0
        return (1+ math.cos(x)) / 2

    def halfsin (t: float, t0: float)->float:
        x = math.pi * ((t / t0) - 1/2)
        y = 1+ math.cos(x)
        return  y / 2

    def log (t: float, t0: float)->float:
        x = (9 * t / t0) + 1
        return math.log(x, 10)

    def invlog (t: float, t0: float)->float:
        if t>=t0:
            return 0
        x = (-9 * t / t0) + 10
        return math.log(x, 10)

    def tri (a, t, t1, t0):
        if t < t1:
            return (t * a) / t1
        else:
            return ((t-t1)/(t1-t0))+a

    def pulses (a, t, t0, t1):
        x = (t/t0) + abs(t/t0)
        # ver porque creo que esta mal
        

