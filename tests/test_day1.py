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

def main():
    unittest.main()

if __name__ == "main":
    main()
