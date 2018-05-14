import json


class Player:
    LOG = "TOR "
    VERSION = "0.0.5"
    rank = {"A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2}

    def get_raise(self, game_state):
        print self.LOG + "get_raise started"
        # current_buy_in - players[in_action][bet] + minimum_raise
        cbuy_in = game_state["current_buy_in"]
        print self.LOG + "current_buy_in " + str(cbuy_in)

        in_action = game_state["in_action"]
        print self.LOG + "in_action " + str(in_action)

        p_bet = game_state["players"][int(in_action)]["bet"]
        min_raise = game_state["minimum_raise"]
        print self.LOG + "minimum_raise " + str(min_raise)

        return cbuy_in - p_bet + min_raise + 1

    def get_player(self, game_state, name):
        print self.LOG + "get_player starts"
        i = 0
        while name != game_state["players"][i]["name"]:
            i = i + 1
        print self.LOG + "get_player returns"
        return game_state["players"][i]

    def get_me(self, game_state):
        print self.LOG + "get_me starts and calls get_player"
        return self.get_player(game_state, unicode("TorMentors"))

    def has_pairs(self, hand):
        return hand[0]["rank"] == hand[1]["rank"]

    def min_value(self, hand):
        return min(self.rank[hand[0]["rank"]], self.rank[hand[1]["rank"]])

    def number_of_players(self, game_state):
        active_count = 0;
        for player in game_state["players"]:
            if player["status"] == "active":
                active_count += 1;
        print self.LOG + "number_of_players is " + str(active_count)
        print json.dumps(game_state, indent=4, sort_keys=True)
        return active_count

    def betRequest(self, game_state):
        try:
            print self.LOG + "game_state:"
            print self.get_me(game_state)

            me = self.get_me(game_state)
            my_hole = me["hole_cards"]
            all_in = me["stack"]

            if self.number_of_players(game_state) > 2:
                value_limit = 12
            else:
                value_limit = 10

            print "my raise: " + str(self.get_raise(game_state))

            if self.has_pairs(my_hole):
                return self.get_raise(game_state)
            if self.min_value(my_hole) > value_limit:
                return self.get_raise(game_state)
            return 0

        except:
            print self.LOG + "exception occured"

        return 0
        
    def showdown(self, game_state):
        pass

