import unittest

from dragon import Dragon


class DragonCreateTest(unittest.TestCase):
    def test_create_dragon_with_name(self):
        dragon = Dragon("Wawelski")

        self.assertIsNotNone(dragon)
        self.assertEqual("Wawelski", dragon.name)
        self.assertGreaterEqual(dragon.health, 50)
        self.assertLessEqual(dragon.health, 100)

    def test_create_dragon_without_name(self):
        with self.assertRaises(ValueError):
            Dragon(None)

    def test_create_dragon_has_random_health_points(self):
        dragon = Dragon("Wawelski")

        self.assertIsNotNone(dragon)
        self.assertGreaterEqual(dragon.health, 50)
        self.assertLessEqual(dragon.health, 100)

    def test_create_dragon_with_default_position(self):
        dragon = Dragon("Wawelski")

        self.assertEqual(0, dragon.x)
        self.assertEqual(0, dragon.y)

    def test_create_dragon_with_initial_position(self):
        dragon = Dragon("Wawelski", x=50, y=100)

        self.assertEqual(50, dragon.x)
        self.assertEqual(100, dragon.y)

    def test_get_position(self):
        dragon = Dragon("Wawelski", x=1, y=2)

        result = dragon.get_position()

        self.assertEqual("(1, 2)", str(result))

    def test_set_position(self):
        dragon = Dragon("Wawelski")

        dragon.set_position(1, 2)

        self.assertEqual(1, dragon.get_position()[0])
        self.assertEqual(2, dragon.get_position()[1])


class DragonPositionChangeTest(unittest.TestCase):
    def create_dragon(self):
        return Dragon("Wawelski", x=10, y=20)

    def test_move_right_by_1(self):
        dragon = self.create_dragon()

        dragon.move_right(1)

        self.assertEqual((11, 20), dragon.get_position())

    def test_move_left_by_1(self):
        dragon = self.create_dragon()

        dragon.move_left(1)

        self.assertEqual((9, 20), dragon.get_position())

    def test_move_down_by_1(self):
        dragon = self.create_dragon()

        dragon.move_down(1)

        self.assertEqual((10, 21), dragon.get_position())

    def test_move_up_by_1(self):
        dragon = self.create_dragon()

        dragon.move_up(1)

        self.assertEqual((10, 19), dragon.get_position())

    def test_move_right_by_1_then_left_by_2(self):
        dragon = self.create_dragon()

        dragon.move_right(1)
        dragon.move_left(2)

        self.assertEqual((9, 20), dragon.get_position())

    def test_move_down_by_1_then_up_by_2(self):
        dragon = self.create_dragon()

        dragon.move_down(1)
        dragon.move_up(2)

        self.assertEqual((10, 19), dragon.get_position())

    def test_move_right_left_down_and_up(self):
        dragon = self.create_dragon()

        dragon.move_right(1)
        dragon.move_left(2)
        dragon.move_down(3)
        dragon.move_up(4)

        self.assertEqual((9, 19), dragon.get_position())


class DragonDamageTest(unittest.TestCase):
    def test_make_damage_is_between_5_and_20(self):
        dragon = Dragon("Wawelski")

        result = dragon.make_damage()

        self.assertGreaterEqual(result, 5)
        self.assertLessEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
