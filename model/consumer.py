# Base class for consumer entities
from shopping_environment import ShoppingEnvironment
from random import random
from numpy.random import normal


class Consumer:
    def __init__(self, env: ShoppingEnvironment):
        self.env = env

        self.abnormal_size  = False
        self.desire         = normal(self.env.mean_desire, self.env.std_desire)
        self.num_shoes_want = 1 if random() < self.env.desire_threshold else 2
        self.money          = normal(self.env.average_mean_money, self.env.average_std_money)
        self.identity       = "average"
        self.has_loyalty    = False

    def printdesire(self):
        print(self.desire)


class AverageConsumer(Consumer):
    pass


class AbnormalConsumer(Consumer):
    def __init__(self):
        self.abnormal_size = True
        self.identity      = "abnormal"