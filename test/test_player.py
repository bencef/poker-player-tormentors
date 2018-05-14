import example
import player
import unittest

class TestPlayer(unittest.TestCase):
    def test_parse_json(self):
        p = player.Player()
        bet = p.betRequest(example.game_state)
        self.assertEqual(5, bet)
