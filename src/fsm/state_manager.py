import sys


class GameStateManager(object):
    """game state manager
    the state manager in the finite state machine of this game
    """
    def __init__(self):
        self.currentState = None

    def changeState(self, newState):
        if self.currentState != None:
            self.currentState.onExit()
        if newState == None:
            sys.exit()
        oldState = self.currentState
        self.currentState = newState
        newState.onEnter(oldState)

    def run(self, initialState):
        self.changeState(initialState)
        while True:
            if self.currentState != None:
                self.currentState.update()
                self.currentState.draw()