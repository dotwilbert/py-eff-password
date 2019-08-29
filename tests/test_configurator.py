#! /usr/bin/env python

import os
import sys
import unittest

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    import gen_eff_pwd as target
else:
    import gen_eff_pwd as target


class TestConfigurator(unittest.TestCase):

    def setUp(self):
        target.Configurator.nuke_config()
        self.no_of_passwords = 5
        self.no_of_words = 5
        self.separator = '-'
        self.postfix = '5$'
        self.capitalize = True
        target.Configurator(self.no_of_passwords, self.no_of_words,
                            self.separator, self.postfix, self.capitalize)
        self.config = target.Configurator.get_config()

    def test_no_of_passwords(self):
        self.assertEqual(self.config.no_of_passwords, self.no_of_passwords,
                         f'Expected number of passwords: {self.no_of_passwords}, actual {self.config.no_of_passwords}')

    def test_no_of_words(self):
        self.assertEqual(self.config.no_of_words, self.no_of_words,
                         f'Expected number of words: {self.no_of_words}, actual {self.config.no_of_words}')
    
    def test_separator(self):
        self.assertEqual(self.config.separator, self.separator,
                         f'Expected separator: {self.separator}, actual {self.config.separator}')

    def test_postfix(self):
        self.assertEqual(self.config.postfix, self.postfix,
                         f'Expected postfix: {self.postfix}, actual {self.config.postfix}')

    def test_capitalize(self):
        self.assertEqual(self.config.capitalize, self.capitalize,
                         f'Expected capitalize: {self.capitalize}, actual {self.config.capitalize}')


if __name__ == '__main__':
    unittest.main()
