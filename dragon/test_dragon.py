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


if __name__ == "__main__":
    unittest.main()
