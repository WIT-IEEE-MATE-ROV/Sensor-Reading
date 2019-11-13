import unittest

from sensor_library import calc_magnitude


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_math():
        print(calc_magnitude(2, 3, 5))


if __name__ == '__main__':
    unittest.main()
