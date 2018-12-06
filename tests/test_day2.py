import unittest
import advent_of_code.day2 as day2

class Day2Tests(unittest.TestCase):

    def test_checksum(self):
        INPUT = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab"
        ]
        print(INPUT)
        self.assertTrue(day2.checksum(INPUT) == 12,
                        msg="Checksum != 12")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
