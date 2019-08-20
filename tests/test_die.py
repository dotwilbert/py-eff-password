#! /usr/bin/env python

import unittest
import sys
import os
if __name__ == '__main__':
    sys.path.append(os.getcwd())
    import gen_eff_pwd as target
else:
    import gen_eff_pwd as target


class TestDie(unittest.TestCase):

    def setUp(self):
        self.die = target.Die()
        self.count_rolls = 1_000_000
        self.error = 0.005
        self.expected_tally = 1.0 / 6.0 * float(self.count_rolls)

    def test_die(self):
        self.rolls = [0, 0, 0, 0, 0, 0]
        for _ in range(self.count_rolls):
            self.rolls[self.die.roll() - 1] += 1

        for i in range(len(self.rolls)):
            self.assertTrue(abs(1 - float(self.rolls[i])/self.expected_tally) <
                            self.error, f'Count of rolls with value {i} is outside of expectation')


if __name__ == '__main__':
    unittest.main()
