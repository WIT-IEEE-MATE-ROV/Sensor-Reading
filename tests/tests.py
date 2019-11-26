import unittest

from filtering import calc_magnitude


class MyTestCase(unittest.TestCase):
    def test_magnitude(self):
        print(calc_magnitude(2, 3, 5))
        self.assertAlmostEquals(calc_magnitude(2, 3, 5), 6.16, 2)


if __name__ == '__main__':
    unittest.main()
