'''Module for building decision trees.

Example tree:
-------------

    {True: (we_have_a_pair,
            {True: (lambda s: num_of_players(s) < 3,
                    {True: 12,
                     False: 0})
             False: 0})}
'''

def run_decision_tree(tree, state):
    '''Given a state and a decision tree run the state machine.  When we
get to a leaf which is a number then return it.'''

    def helper(last_result, tree):
        leaf = tree[last_result]

        if isinstance(leaf, int):
            return leaf

        predicate =  leaf[0]
        new_tree = leaf[1]

        return helper(predicate(state), new_tree)

    return helper(True, tree)
