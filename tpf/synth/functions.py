
from cmath import cos
import matplotlib.pyplot as plt
import numpy as np

def constant (t: float, x )->float:
    return t*1

def linear (t: float, t0: float)->float:
    return t/t0

def invlinear (t: float, t0: float)->float:
    return np.where(0<t<t0, 1-(t/t0), 0) 

def sin (a: float, t: float, f: float)->float:
    x = f*t
    return 1 + a * np.sin(x)

def exp (t: float, t0: float)->float:
    x = 5*(t-t0)/t0
    return np.exp(x)

def invexp (t: float, t0: float)->float:
    x = -5*t/t0
    return np.exp(x)

def quartcos (t: float, t0: float)->float:
    x = (np.pi * t) / 2 * t0
    return np.cos(x)

def quartsin (t: float, t0: float)->float:
    x = (np.pi * t) / 2 * t0
    return np.sin(x)
    
def halfcos (t: float, t0: float)->float:
    x = (np.pi * t) / t0
    return (1+ np.cos(x)) / 2

def halfsin (t: float, t0: float)->float:
    x = np.pi * ((t / t0) - 1/2)
    y = 1+ np.cos(x)
    return  y / 2

def log (t: float, t0: float)->float:
    x = (9 * t / t0) + 1
    return np.log10(x)

def invlog (t: float, t0: float)->float:
        x = (-9 * t / t0) + 10
        return np.where(t>=t0, 0, np.log10(x) )
     
def tri (a, t, t1, t0):
    return np.where(t < t1, (t * a) / t1, ((t-t1)/(t1-t0))+a )
    
def pulses (a, t, t0, t1):
    x = (t/t0) + abs(t/t0)
    return np.where(1 > x, x, 1) 
    
    
# set functions
attack = {
    'LINEAR' : linear,
    'EXP' : exp,
    'QUARTSIN' : quartsin,
    'HALFSIN' : halfsin,
    'LOG' : log,
    'TRI' : tri,
    }

sustain = {
    'CONSTANT': constant,
    'INVLINEAR' : invlinear,
    'SIN' : sin,
    'INVEXP' : invexp,
    'QUARTCOS' : quartcos,
    'HALFCOS' : halfcos,
    'INVLOG' : invlog, 
    'PULSES' : pulses
}

decay = {
    'INVLINEAR' : invlinear,
    'INVEXP' : invexp,
    'QUARTCOS' : quartcos,
    'HALFCOS' : halfcos,
    'INVLOG' : invlog, 
}

# validate floats
def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    
