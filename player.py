
class Player:
    LOG = "TOR "
    VERSION = "0.0.4"
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
        return len(game_state["players"])

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

            if self.has_pairs(my_hole):
                return all_in
            if self.min_value(my_hole) > value_limit:
                return all_in
            return 0

        except:
            print self.LOG + "exception occured"

        return 0
        
    def showdown(self, game_state):
        pass

