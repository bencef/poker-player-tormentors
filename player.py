
class Player:
    VERSION = "0.0.1"

    def get_player(self, game_state, name):
        print "02"
        i = 0
        while name != game_state["players"][i]:
            i = i + 1
        print "03"
        return game_state["players"][i]

    def get_me(self, game_state):
        print "01"
        return self.get_player(game_state, unicode("TorMentors"))

    def betRequest(self, game_state):
        try:
            print "me me me:"
            print self.get_me(game_state)

            myStack = game_state["players"]
            print '0 {0}'.format(myStack)
            
            myStack = game_state["players"][0]
            print '1 {0}'.format(myStack)
            
            myStack = game_state["players"][0]["name"]
            print '2 {0}'.format(myStack)
            
            myStack = game_state["players"][0]["stack"]
            print '3 {0}'.format(myStack)

        except:
            print "exception occured"
        return 1000
        
    def showdown(self, game_state):
        pass

