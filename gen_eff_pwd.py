#! /usr/bin/env python

import secrets


class Die:

    def __init__(self):
        self.die = secrets.SystemRandom()

    def roll(self) -> int:
        return self.die.randint(1, 6)
