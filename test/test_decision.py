import unittest
import state.transitions as st

def we_have_a_pair(state):
    return state['we_have_a_pair']

def number_of_enemies(state):
    return state['number_of_enemies']

decision_tree = {True: (we_have_a_pair,
                        {True: (lambda s: number_of_enemies(s) > 2,
                                {True: 1,
                                 False: 2}),
                         False: 3})}

class TestDecision(unittest.TestCase):

    def test_have_pair_two_enemies(self):
        state = {'number_of_enemies': 2,
                 'we_have_a_pair': True}
        self.assertEqual(2, st.run_decision_tree(decision_tree, state))

    def test_have_pair_three_enemies(self):
        state = {'number_of_enemies': 3,
                 'we_have_a_pair': True}
        self.assertEqual(1, st.run_decision_tree(decision_tree, state))

    def test_have_no_pair(self):
        state = {'number_of_enemies': 3,
                 'we_have_a_pair': False}
        self.assertEqual(3, st.run_decision_tree(decision_tree, state))
