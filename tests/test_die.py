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
        0.1:    9.236,
        0.05:  11.070,
        0.025: 12.833,
        0.02:  13.388,
        0.01:  15.086,
        0.005: 16.750
    }

    def setUp(self):
        self.count_rolls = 100_000
        self.pvalue = 0.1
        self.expected_tally = 1.0 / 6.0 * float(self.count_rolls)
        self.number_of_votes = 11
        self.failures_threshold = 4

    def chisquare_accept_fair(self) -> bool:
        die = target.Die()
        rolls = [0, 0, 0, 0, 0, 0]
        for _ in range(self.count_rolls):
            rolls[die.roll() - 1] += 1
        # null-hypothesis: die is not biased
        # calculate chi-squared statistic
        cv = 0
        for i in range(len(rolls)):
            cv += ((rolls[i] - self.expected_tally) ** 2) / self.expected_tally
        return cv < self.chisq_at_5df[self.pvalue]

    def test_die(self):
        # run experiment
        failure_count = 0
        for _ in range(self.number_of_votes):
            if not self.chisquare_accept_fair():
                failure_count += 1
        self.assertLessEqual(
            failure_count, self.failures_threshold, 'the die does not appear to be unbiased')


if __name__ == '__main__':
    unittest.main()
