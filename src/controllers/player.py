from models.player import *
from random import randint


class PlayerController(object):
    """MVC Player controller class
    player entity controller in the MVC pattern put in place
    """
    def __init__(self, isComputer):
        self.model = PlayerModel("Computer" if isComputer else "Player", isComputer)
        self.isComputer = isComputer

    def update(self, input):
        if self.isComputer:
            self.model.move = ['R', 'P', 'S'][randint(0,2)]
        else:
            self.model.move = input