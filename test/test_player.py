import example
import player
import unittest

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = player.Player()

    def test_nine_pair(self):
        our_cards = pair_of('9')
        game_state = example.make_game_state(our_cards, 2, 10)
        bet = self.player.betRequest(game_state)
        self.assertTrue(0 < bet)

    def test_eight_pair(self):
        our_cards = pair_of('8')
        game_state = example.make_game_state(our_cards, 3, 15)
        bet = self.player.betRequest(game_state)
        self.assertEqual(0, bet)

################################################################################
# Helpers
################################################################################

def pair_of(rank):
    '''Return a pair of a given rank in a format passable to
make_game_state.'''

    return [{'rank': rank, 'suit': 'hearts'},
            {'rank': rank, 'suit': 'spades'}]
