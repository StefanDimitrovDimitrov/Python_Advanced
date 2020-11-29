from testing.cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_init(self):
        self.assertEqual(self.cat.name, "Tom")

    def test_cat_increases_seize_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_eat_if_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc:
            self.cat.eat()
        self.assertEqual(str(exc.exception), 'Already fed.')

    def test_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(str(exc.exception), 'Cannot sleep while hungry')

    def test_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()