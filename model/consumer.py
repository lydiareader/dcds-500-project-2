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
        self.has_loyalty    = random() < self.env.average_prob_loyal
        self.shoes_acquired = 0

    def printdesire(self):
        print(self.desire)

    
    def buy_shoes(self):
        self.env.num_shoes = self.env.num_shoes - 1
        self.shoes_acquired = 1


class AverageConsumer(Consumer):
    pass


class AbnormalConsumer(Consumer):
    def __init__(self, env):
        Consumer.__init__(self, env)
        self.abnormal_size = True
        self.identity      = "abnormal"


class SpecialConsumer(Consumer):
    def __init__(self, env):
        Consumer.__init__(self, env)
        self.num_shoes_want = 2
        self.identity       = "special"


class WealthyConsumer(Consumer):
    def __init__(self, env):
        Consumer.__init__(self, env)
        self.money       = normal(self.env.rich_mean_money, self.env.rich_std_money)
        self.has_loyalty = random() < self.env.rich_prob_loyal
        self.identity    = "wealthy"


class InfluencerConsumer(WealthyConsumer):
    def __init__(self, env):
        WealthyConsumer.__init__(self, env)
        self.identity = "influencer"


class ResellerConsumer(Consumer):
    def __init__(self, env):
        Consumer.__init__(self, env)
        #TODO: further define these values
        self.desire         = 0
        self.num_shoes_want = 100
        self.money          = 100000
        self.has_loyalty    = random() < self.env.reseller_prob_loyal
        self.identity       = "reseller"