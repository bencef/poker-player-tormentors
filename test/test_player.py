import example
import player
import unittest

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = player.Player()

    def test_nine_pair_with_1_enemy_and_2_sb(self):
        our_cards = pair_of('9')
        game_state = example.make_game_state(our_cards, 1, 2)
        bet = self.player.betRequest(game_state)
        self.assertTrue(0 < bet)

    def test_nine_pair_with_1_enemy_and_10_sb(self):
        our_cards = pair_of('9')
        game_state = example.make_game_state(our_cards, 1, 10)
        bet = self.player.betRequest(game_state)
        self.assertTrue(0 < bet)

    def test_nine_pair_with_1_enemy_and_20sb(self):
        our_cards = pair_of('9')
        game_state = example.make_game_state(our_cards, 1, 20)
        bet = self.player.betRequest(game_state)
        self.assertTrue(0 < bet)

    def test_nine_pair_with_1_enemy_and_20sb(self):
        our_cards = pair_of('9')
        game_state = example.make_game_state(our_cards, 1, 40)
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
