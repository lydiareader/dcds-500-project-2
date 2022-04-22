from random import random

class Accounts:
    def __init__(self, loyalty_prob):
        self.has_loyalty    = random() < loyalty_prob