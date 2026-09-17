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


if __name__ == "__main__":
    unittest.main()
