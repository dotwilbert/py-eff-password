#! /usr/bin/env python

import unittest
import sys
import os
if __name__ == '__main__':
    sys.path.append(os.getcwd())
    import gen_eff_pwd as target
else:
    import gen_eff_pwd as target


class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.pwg = target.PasswordGenerator()

    def test_password_generator(self):
        pw = self.pwg.generate_password()
        self.assertTrue( pw in target.PasswordGenerator.eff_wordlist.values(), f'unexpected value {pw} for generated password')


if __name__ == '__main__':
    unittest.main()
