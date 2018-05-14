'''Probability distributions are represented as lists of tuples such
(event, probability) where the probability of all events addd up to
1.0'''

from util import *

def certainly(value):
    '''A probability distribution with one outcome which has absolute
certainity.'''

    return [(value, 1.0)]

def uniform(values):
    '''A probability distribution with all the values having the same
probability.'''

    probability = 1.0 / len(values)
    return  [(v, probability) for v in values]

def enumerated(values, probabilities):
    '''A probability distribution with every value mapped to corresponding
probability.'''

    v_len = len(values)
    p_len = len(probabilities)

    if v_len != p_len:
        raise ValueError('Length of value and probabilities should match.')

    if not float_close(sum(probabilities), 1.0, 0.00001):
        raise ValueError('Probabilities should add up to 1.0')

    return zip(values, probabilities)
