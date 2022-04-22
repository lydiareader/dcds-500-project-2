from random import random

class Account:
    def __init__(self, person):
        self.has_loyalty    = random() < person.prob_loyal
        self.person         = person 