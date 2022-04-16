# Base class for consumer entities
from random import random
from numpy.random import normal


class Consumer:
    def __init__(self, env):
        self.env = env

        self.abnormal_size  = False
        self.desire         = normal(self.env.mean_desire, self.env.std_desire)
        self.num_shoes_want = 1 if random() < self.env.desire_threshold else 2
        self.money          = normal(self.env.average_mean_money, self.env.average_std_money)
        self.identity       = "average"
        self.has_loyalty    = random() < self.env.average_prob_loyal
        self.shoes_acquired = 0


    def buy_shoes(self, cap):
        self._buy_shoes(min(cap, self.num_shoes_want, self.env.num_shoes))
        #TODO: incorporate money

    
    def reset(self):
        self.shoes_acquired = 0


    def _buy_shoes(self, num_to_buy):
        self.env.num_shoes = self.env.num_shoes - num_to_buy
        self.shoes_acquired += num_to_buy


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

    def buy_shoes(self, cap):
        # special consumer will not buy 1 pair, only 2 pairs
        if self.env.num_shoes >= 2:     #TODO: incorporate money
            self._buy_shoes(2)


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