from random import randint


class Dragon:
    def __init__(self, name, x=0, y=0):
        if not name:
            raise ValueError("Dragon must have a name")
        self.name = name
        self.health = randint(50, 100)
        self.x = x
        self.y = y

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move_right(self, value):
        self.x += value

    def move_left(self, value):
        self.x -= value

    def move_up(self, value):
        self.y -= value

    def move_down(self, value):
        self.y += value

    def move_horizontal(self, right=0, left=0):
        self.move_right(right)
        self.move_left(left)

    def move_vertical(self, up=0, down=0):
        self.move_up(up)
        self.move_down(down)

    def move(self, right=0, left=0, up=0, down=0):
        self.move_horizontal(right=right, left=left)
        self.move_vertical(up=up, down=down)

    def make_damage(self):
        return randint(5, 20)
