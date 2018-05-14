import example
import player
import unittest

class TestPlayer(unittest.TestCase):

    def test_ace_pair(self):
        p = player.Player()
        our_cards = pair_of('A')
        bet = p.betRequest(example.make_game_state(our_cards))
        self.assertTrue(0 < bet)

################################################################################
# Helpers
################################################################################

def pair_of(rank):
    '''Return a pair of a given rank in a format passable to
make_game_state.'''

    return [{'rank': rank, 'suit': 'hearts'},
            {'rank': rank, 'suit': 'spades'}]
