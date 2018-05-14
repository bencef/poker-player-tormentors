'''Module for representing cards.  In the JSON they are represented as
{
    "rank": "6",     // Rank of the card. Possible values are numbers 2-10 and J,Q,K,A
    "suit": "hearts" // Suit of the card. Possible values are: clubs,spades,hearts,diamonds
}
'''

class Card():
    '''Class representing a card.'''

    def __init__(self, json_card):
        '''Create a card object from a JSON object representing a card.'''

        try:
            self.rank = to_number(json_card['rank'])
            self.suit = json_card['suit']
        except KeyError:
            raise ValueError('card is not initialised from '
                             + 'a JSON object representing a card.')


################################################################################
# Utility functions
################################################################################

def to_number(card_str):
    '''Convert a rank represented as a character to an integer
representation.'''
    try:
        return int(card_str)
    except ValueError:
        return {'J': 11, 'Q': 12, 'K': 13, 'A': 14}[card_str]
