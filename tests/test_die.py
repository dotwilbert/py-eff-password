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

    chisq_at_5df = {
        0.05:  11.070,
        0.025: 12.833,
        0.02:  13.388,
        0.01:  15.086,
        0.005: 16.750
    }

    def setUp(self):
        self.die = target.Die()
        self.count_rolls = 100_000
        self.pvalue = 0.01
        self.expected_tally = 1.0 / 6.0 * float(self.count_rolls)

    def test_die(self):
        # run experiment
        self.rolls = [0, 0, 0, 0, 0, 0]
        for _ in range(self.count_rolls):
            self.rolls[self.die.roll() - 1] += 1

        # null-hypothesis: die is not biased
        # calculate chi-squared statistic
        cv = 0
        for i in range(len(self.rolls)):
            cv += ((self.rolls[i] - self.expected_tally)
                   ** 2) / self.expected_tally
        self.assertLess(
            cv, self.chisq_at_5df[self.pvalue], 'the die does not appear to be unbiased')

#        for i in range(len(self.rolls)):
#            self.assertTrue(abs(1 - float(self.rolls[i])/self.expected_tally) <
#                            self.error_ratio, f'Rolls of {i+1}\'s: Expected: {self.expected_tally:,.2f}, actual {self.rolls[i]:,}. This can happen by chance, but should be rare. Run the test again')


if __name__ == '__main__':
    unittest.main()
