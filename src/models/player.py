class PlayerModel(object):
    """MVC Player model class
    """
    def __init__(self, name, isComputer):
        self.move = None
        self.score= 0
        self.name = name
        self.isComputer = isComputer