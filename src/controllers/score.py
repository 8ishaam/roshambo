from config.reader import conf

class ScoreController(object):
    """Score controller class
    The game score logic, updates the player controllers
    """
    def __init__(self, players):
        self.p1 = players[0]
        self.p2 = players[1]

    def update(self, input):
        self.p1.update(input)
        self.p2.update(input)
        if conf["power_matrix"].get(self.p1.model.move) == self.p2.model.move:
            self.p1.model.score += 1
        else:
            self.p2.model.score += 1

    def getWinner(self):
        if self.p1.model.score == 3:
            return self.p1
        elif self.p2.model.score == 3:
            return self.p2
        else:
            None