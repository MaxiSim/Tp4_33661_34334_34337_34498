import numpy as np

# math functions to modulate the amplitude of each note
def constant (t: float, x = 1 )->float:
    """
    The constant function returns 1 for all values of t.
    
    Parameters:
        t (float): The time at which the function is evaluated.  
    
        x (float): A dummy argument that does nothing, but is required so that the genereic function can be called;
    
    :param t:float: Specify that the function takes a single parameter, t, which is of type float.
    :param x=1: Indicate that the constant function is used to represent a constant value.
    :return: Array of 1s of the same length as t
    """
    return np.ones_like(t) 

def linear (t: float, t0: float)->float:
    """
    The linear function takes in a float t and returns t.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used to determine the slope of the function.
    :return: The value of t divided by t0.
    """
    return t/t0

def invlinear (t: float, t0: float)->float:
    """
    The invlinear function returns the inverse of a linear function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used to determine the slope of the function.
    :return: The inverse of the linear function
    """
    return np.where(t>t0, 0, 1-(t/t0))


def sin (t: float, a: float, f: float)->float:
    """
    The sin function returns a sine function.
    
    :param t:float: The time at which the function is evaluated.
    :param a:float: Parameter that is used to determine amplitude of the function.
    :param f:float: Parameter that is used to determine frequency of the function.
    :return: The sine function for a determined time range, amplitude, and frequency.
    """
    x = f*t
    return 1 + a * np.sin(x)

def exp (t: float, t0: float)->float:
    """
    The exp function returns an exponential function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used to determine the slope of the function.
    :return: The exponential function for a determined time range, and slope.
    """
    x = 5*(t-t0)/t0
    return np.exp(x)

def invexp (t: float, t0: float)->float:
    """
    The invexp function returns the inverse of an exponential function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used to determine the slope of the function.
    :return: The inverse of the exponential function for a determined time range, and slope.
    """
    x = -5*t/t0
    return np.exp(x)

def quartcos (t: float, t0: float)->float:
    """
    The quartcos function returns a cosine function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used by the function.
    :return: The cosine function for a determined time range.
    """
    x = (np.pi * t) / (2 * t0)
    return np.cos(x)

def quartsin (t: float, t0: float)->float:
    """
    The quartsin function returns a sine function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used by the function.
    :return: The sine function for a determined time range.
    """
    x = (np.pi * t) / 2 * t0
    return np.sin(x)
    
def halfcos (t: float, t0: float)->float:
    """
    The halfcos function returns half of the cosine function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used by the function.
    :return: The half of the cosine function for a determined time range.
    """
    x = (np.pi * t) / t0
    return (1+ np.cos(x)) / 2

def halfsin (t: float, t0: float)->float:
    """
    The halfsin function returns half of the sine function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used by the function.
    :return: The half of the sine function for a determined time range.
    """
    x = np.pi * ((t / t0) - 1/2)
    y = 1+ np.cos(x)
    return  y / 2

def log (t: float, t0: float)->float:
    """
    The log function returns a log function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used by the function.
    :return: The log function for a determined time range.
    """
    x = (9 * t / t0) + 1
    return np.log10(x)

def invlog (t: float, t0: float)->float:
    """
    The invlog function returns the inverse of the log function.
    
    :param t:float: The time at which the function is evaluated.
    :param t0:float: Parameter that is used by the function.
    :return: The inverse of a log function for a determined time range.
    """
    x = (-9 * t / t0) + 10
    return np.where(t>=t0, 0, np.log10(x) )
     
def tri (t, a, t1, t0):
    """
    The tri function returns a value depending on weather t is bigger than t1 or not.
    
    :param t:float: The time at which the function is evaluated.
    :param a:float: Parameter that is used to determine amplitude of the function.
    :param t1:float: Parameter that is used by the function.
    :param t0:float: Parameter that is used by the function.
    :return: The values of t evaluated in the function depending on weather t is bigger than t1 or not.
    """
    return np.where(t < t1, (t * a) / t1, ((t-t1)/(t1-t0))+a )
    
def pulses (t, a, t0, t1):
    """
    The pulses function returns a value depending the result of the equation y bigger than 1 or not.
    
    :param t:float: The time at which the function is evaluated.
    :param a:float: Parameter that is used to determine amplitude of the function.
    :param t0:float: Parameter that is used by the function.
    :param t1:float: Parameter that is used by the function.
    :return: 1 if the equations result is bigger than 1, or the result of the equation if it is lower than 1.
    """
    x = (1-a / t1) * (t - t0 + t1)
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
    """
    The isfloat function checks if a string is composed by floats or not.
    
    :param x:str: string taken from either a music sheet or the instrument setup file.
    :return: Wehther the string is composed by floats or not.
    """
    try:
        float(x)
        return True
    except ValueError:
        return False
    
