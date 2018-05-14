
class Player:
    VERSION = "0.0.1"

    def betRequest(self, game_state):
        try:
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

