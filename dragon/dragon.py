from random import randint


class Dragon:
    def __init__(self, name, x=0, y=0):
        if not name:
            raise ValueError("Dragon must have a name")
        self.name = name
        self.health = randint(50, 100)
        self.x = x
        self.y = y
