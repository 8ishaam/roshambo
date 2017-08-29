from config.reader import conf

class PlayerView(object):
    """MVC Player view class
    """
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        print(self.controller.model.name.upper() + " -"*10)
        print(conf["labels"]["EN"]["last_move"] % self.controller.model.move)
        print(conf["labels"]["EN"]["score"] % self.controller.model.score)
        print("- "*10)
        print("")