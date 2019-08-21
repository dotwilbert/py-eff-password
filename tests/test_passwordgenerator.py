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
        self.pwg = target.PasswordGenerator(1)

    def test_password_generator(self):
        pw = self.pwg.generate_password()
        self.assertTrue( pw in target.PasswordGenerator.eff_wordlist.values(), f'unexpected value {pw} for generated password')
    
    def test_number_of_words(self):
        die = target.Die()
        sep = '-'
        # Some random number from 3 to 8, both included.
        no_of_words = 9 - die.roll()
        self.pwg.number_of_words = no_of_words
        self.pwg.separator = sep
        word_list = self.pwg.generate_password().split(sep)
        self.assertEqual( no_of_words, len(word_list), 'generated password does not have the expected number of words')
        for w in word_list:
            self.assertTrue( w in target.PasswordGenerator.eff_wordlist.values(), f'unexpected value {w} in generated password' )

    def test_postfix(self):
        postfix = '5$'
        self.pwg = target.PasswordGenerator(number_of_words=1, postfix=postfix)
        self.assertTrue( self.pwg.postfix == postfix, f'postfix expected: {postfix}, actual: {self.pwg.postfix}')
        pw = self.pwg.generate_password()
        self.assertTrue(pw.endswith(postfix), f'end characters in {pw} do not match given postfix: {postfix}')


if __name__ == '__main__':
    unittest.main()
