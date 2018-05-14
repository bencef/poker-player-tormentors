import json


class Player:
    LOG = "TOR "
    VERSION = "0.1.0"
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

    def get_minimum_raise(self, game_state):
        min_raise = game_state["minimum_raise"]
        print self.LOG + "minimum_raise " + str(min_raise)
        return self.get_call(game_state) + min_raise

    def get_call(self, game_state):
        print self.LOG + "get_raise started"
        # current_buy_in - players[in_action][bet] + minimum_raise
        cbuy_in = game_state["current_buy_in"]
        print self.LOG + "current_buy_in " + str(cbuy_in)

        in_action = game_state["in_action"]
        print self.LOG + "in_action " + str(in_action)

        p_bet = game_state["players"][int(in_action)]["bet"]
        return cbuy_in - p_bet

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

    def max_value(self, hand):
        return max(self.rank[hand[0]["rank"]], self.rank[hand[1]["rank"]])

    def number_of_players(self, game_state):
        active_count = 0
        for player in game_state["players"]:
            if player["status"] == "active":
                active_count += 1
        print self.LOG + "number_of_players is " + str(active_count)
        print json.dumps(game_state, indent=4, sort_keys=True)
        return active_count

    def get_limit_decrease_by_blind(self, small_blind):
        # 2  3  5  10 15 20 30 (small blind)
        # 10 20 30 40 50 60 70 (game num)
        if small_blind <= 5:
            return 0
        elif small_blind <= 15:
            return 1
        elif small_blind <= 30:
            return 2
        else:
            return 3

    def get_bet(self, hand_min, hand_max, active_enemies, small_blind, min_raise, all_in):
        decr = self.get_limit_decrease_by_blind(small_blind)
        if hand_min == hand_max:
            if active_enemies > 1:
                if hand_min >= 12 - decr:
                    return all_in
                elif hand_min >= 9 - decr:
                    return min_raise
                else:
                    return 0
            else:
                if hand_min >= 10 - decr:
                    return all_in
                elif hand_min >= 4 - decr:
                    return min_raise
                else:
                    return 0
        else:
            if active_enemies > 2:
                if hand_min >= 13 - decr:
                    return min_raise
                else:
                    return 0
            else:
                if hand_min >= 11 - decr:
                    return min_raise
                else:
                    return 0

    def betRequest(self, game_state):
        try:
            print self.LOG + "game_state:"
            print self.get_me(game_state)

            me = self.get_me(game_state)
            my_hand = me["hole_cards"]

            hand_min = self.min_value(my_hand)
            hand_max = self.max_value(my_hand)
            min_raise = self.get_minimum_raise(game_state)
            all_in = me["stack"]
            small_blind = int(game_state["small_blind"])
            active_enemies = self.number_of_players(game_state)

            return self.get_bet(hand_min, hand_max, active_enemies, small_blind, min_raise, all_in)

        except:
            print self.LOG + "exception occured"

        return 0
        
    def showdown(self, game_state):
        pass

