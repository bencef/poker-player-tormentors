import example
import player
import unittest

class TestPlayer(unittest.TestCase):
    def test_ace_pair(self):
        p = player.Player()
        our_cards = [{'rank': 'A', 'suit': 'hearts'},
                     {'rank': 'A', 'suit': 'spades'}]
        bet = p.betRequest(example.make_game_state(our_cards))
        self.assertEqual(480, bet)
