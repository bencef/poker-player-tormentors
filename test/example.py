import json

def make_game_state(our_cards):

    return {
        u'tournament_id':u'550d1d68cd7bd10003000003',

  u'game_id':u'550da1cb2d909006e90004b1',



  u'round':0,

  u'bet_index':0,

  u'small_blind': 10,


  u'current_buy_in': 320,

  u'pot': 400,

  u'minimum_raise': 240,


  u'dealer': 1,


  u'orbits': 7,


  u'in_action': 1,

  u'players': [
      {

          u'id': 0,

          u'name': u'Albert',

          u'status': u'active',





          u'version': u'Default random player',

          u'stack': 1010,


          u'bet': 320
      },
      {
          u'id': 1,
          u'name': u'TorMentors',
          u'status': u'active',
          u'version': u'Default random player',
          u'stack': 1590,
          u'bet': 80,
          u'hole_cards': [

              {
                  u'rank': our_cards[0]['rank'],
                  u'suit': our_cards[0]['suit']
              },
              {
                  u'rank': our_cards[1]['rank'],
                  u'suit': our_cards[1]['suit']
              }
          ]
      },
      {
          u'id': 2,
          u'name': u'Chuck',
          u'status': u'out',
          u'version': u'Default random player',
          u'stack': 0,
          u'bet': 0
      }
  ],
        u'community_cards': [
            {
                u'rank': u'4',
                u'suit': u'spades'
            },
            {
                u'rank': u'A',
                u'suit': u'hearts'
            },
            {
                u'rank': u'6',
                u'suit': u'clubs'
            }
        ]
    }
