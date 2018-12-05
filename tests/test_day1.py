import unittest
import advent_of_code.day1 as day1

class Day1Tests(unittest.TestCase):

    def test_freq_addition(self):
        self.assertTrue(day1.freq_addition([+1, +1, +1]) == 3,
                        msg="Addition of frequencies != 3")

        self.assertTrue(day1.freq_addition([+1, +1, -2]) == 0,
                        msg="Addition of frequencies != 0")

        self.assertTrue(day1.freq_addition([-1, -2, -3]) == -6,
                        msg="Addition of frequencies != -6")

    def test_repeat_freq(self):
        self.assertTrue(day1.repeat_freq([+1, -1]) == 0,
                        msg="Repeated frequency != 0")

        self.assertTrue(day1.repeat_freq([+3, +3, +4, -2, -4]) == 10,
                        msg="Repeated frequency != 10")

        self.assertTrue(day1.repeat_freq([-6, +3, +8, +5, -6]) == 5,
                        msg="Repeated frequency != 5")

        self.assertTrue(day1.repeat_freq([+7, +7, -2, -7, -4]) == 14,
                        msg="Repeated frequency != 14")


def main():
    unittest.main()

if __name__ == "main":
    main()
