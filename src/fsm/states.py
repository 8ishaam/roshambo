"""Finite state machine states
each state class represents a state/screen of the game
"""
from controllers.player import *
from controllers.score import *
from views.player import *
from utils.input import get_input
from config.reader import conf
import time, os

# os porting taking into account, clear for unix based systems and cls for windows
CLEAR_COMMAND = conf["porting"]["cmd"]["clear"]["windows" if os.name == "nt" else "other_os"]

class GameState(object):
    """Base class for game states
    """
    def __init__(self, game):
        self.game = game

    def onEnter(self, previousState):
        pass

    def onExit(self):
        pass

    def update(self):
        pass

    def draw(self, noprompt=False):
        pass


class MessageDisplayState(GameState):
    """Message display state
    intermediate state for the purpose of displaying a temporary message screen
    """
    def __init__(self, game, msg, nextState):
        super(MessageDisplayState, self).__init__(game)
        self.msg = msg
        self.nextState = nextState

    def onEnter(self, previousState):
        os.system(CLEAR_COMMAND)
        previousState.draw(noprompt=True)
        time.sleep(2)

    def update(self):
        time.sleep(5)
        self.game.changeState(self.nextState)

    def draw(self, noprompt=False):
        print(self.msg.upper() + "!!!!!")
        print(conf["messages"]["EN"]["redirect"])


class PlayingGameState(GameState):
    """Play game state
    the main action state, where the game is actually happening
    """
    def __init__(self, game, gameOverState, gameWonState):
        super(PlayingGameState, self).__init__(game)
        self.controller = None
        self.views = None
        self.game = game
        self.gameOverState = gameOverState
        self.gameWonState = gameWonState
        self.mode = None
        self.input = None

    def initialize(self):
        params = (True, True)
        if self.mode == 1: # P vs C
            params = (False, True)
        elif self.mode == 2: # C vs C
            params = (True, True)
        else:
            pass # should not happen
        playerControllers = map(PlayerController, params)
        self.controller = ScoreController(playerControllers)
        self.views = map(PlayerView, playerControllers)

    def update(self):
        self.controller.update(self.input)
        winner = self.controller.getWinner()
        if winner is not None and winner.isComputer:
            self.game.changeState(self.gameOverState)
        elif winner is not None and not winner.isComputer:
            self.game.changeState(self.gameWonState)

    def draw(self, noprompt=False):
        os.system(CLEAR_COMMAND)
        for view in self.views:
            view.render()
        if self.mode == 1 and not noprompt: # P vs C mode's prompt for Player input
            self.input = get_input(conf["messages"]["EN"]["play_prompt"], conf["patterns"]["move_input"])
            while self.input is None:
                print(conf["messages"]["EN"]["invalid_input"])
                self.input = get_input("\n> ", conf["patterns"]["move_input"])
            self.input = self.input.upper()
        elif self.mode == 2: # C vs C mode, automatically display a basic progress bar
            for i in xrange(5, 0, -1):
                print("*"*i)
                time.sleep(1)
        else:
            pass # nothing happens

class MainMenuState(GameState):
    """Main menu state
    the start state
    """
    def __init__(self, game):
        super(MainMenuState, self).__init__(game)
        self.playGameState = None
        self.choice = None

    def setPlayingState(self, state):
        self.playGameState = state

    def update(self):
        if self.choice is not None:
            if self.choice in ('1', '2'):
                self.playGameState.mode = int(self.choice)
                self.playGameState.initialize()
                self.game.changeState(self.playGameState)
            else:
                self.game.changeState(None)

    def draw(self, noprompt=False):
        os.system(CLEAR_COMMAND)
        print("$$$$$$$$$$$$$$$$$$$")
        print("$$$   Welcome   $$$")
        print("$$$     To      $$$")
        print("$$$  ROSHAMBO   $$$")
        print("$$$$$$$$$$$$$$$$$$$")
        print("")
        self.choice = get_input(conf["messages"]["EN"]["main_menu_prompt"], )
        while self.choice is None:
            print(conf["messages"]["EN"]["invalid_input"])
            self.choice = get_input("\n> ", conf["patterns"]["move_input"])