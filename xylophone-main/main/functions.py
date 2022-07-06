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
    