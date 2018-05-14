'''Utility functions used only internally.'''

def float_close(a, b, eta):
    '''Determine if two floating point numbers are close enough.'''

    diff = abs(a - b)

    return diff < eta
