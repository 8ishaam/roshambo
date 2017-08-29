#!/usr/bin/python

"""Main script for running the game
"""
import sys
sys.path.append("src")

from os import environ, path
environ["ROSHAMBO_CONFFILE"] = path.join(path.abspath(path.curdir), "conf.json")

from fsm.states import *
from fsm.state_manager import *
from config.reader import conf


roshamboGame = GameStateManager()
mainMenuState = MainMenuState(roshamboGame)
gameWonState = MessageDisplayState(roshamboGame, conf["messages"]["EN"]["you_win"], mainMenuState)
gameOverState = MessageDisplayState(roshamboGame, conf["messages"]["EN"]["game_over"], mainMenuState)
playingGameState = PlayingGameState(roshamboGame, gameOverState, gameWonState)
mainMenuState.setPlayingState(playingGameState)

roshamboGame.run(mainMenuState)
