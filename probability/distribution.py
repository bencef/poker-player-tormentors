'''Probability distributions are represented as lists of tuples such
(event, probability) where the probability of all events addd up to
1.0'''

from util import *

################################################################################
# Constructors
################################################################################

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

################################################################################
# Getters
#
# Mostly for internal use.  Avoid these outside of this file.  Rather
# write well named functions.
################################################################################

def probability(event):
    '''Get the probability of an event.'''

    return event[1]

def value(event):
    '''Get the value of an event.'''

    return event[0]

################################################################################
# Operations on distributions
################################################################################

def as_percent(predicate, distribution):
    '''Return as a floating point number [0.0, 1.0] the chance of a
predicate holding true in a distribution.

Example usage:
--------------

    >>> import probability.distribution as dis
    # Six sided dice
    >>> die6 = dis.uniform(range(1, 7))
    >>> die6
    [(1, 0.16666666666666666), (2, 0.16666666666666666)...
    # chance of throwing bigger than 4
    >>> dis.as_percent(lambda v: v > 4, die6)
    0.3333333333333333
'''

    return sum([probability(event)
                for event in distribution
                if predicate(value(event))])
