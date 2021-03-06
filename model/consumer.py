# Base class for consumer entities
from random import random
from numpy.random import normal
import accounts


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
        self.influence      = 0
        self.proxy          = self.desire
        self.got_shoes      = False
        self.prob_loyal     = self.env.average_prob_loyal
        self.main_account   = accounts.Account(self)
        self.fake_accounts  = [accounts.Account(self)] if self.num_shoes_want > 1 else []

        self.authorized_fake_accounts = []

    def buy_shoes(self, cap):
        self._buy_shoes(min(cap, self.num_shoes_want - self.shoes_acquired, self.env.num_shoes))
        if self.shoes_acquired > 0 : self.got_shoes = True

    
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
        if self.env.num_shoes >= 2 and cap > 1 and self.shoes_acquired < 2:
            self._buy_shoes(2)
            self.got_shoes = True


class WealthyConsumer(Consumer):
    def __init__(self, env):
        Consumer.__init__(self, env)
        self.money          = normal(self.env.rich_mean_money, self.env.rich_std_money)
        self.has_loyalty    = random() < self.env.rich_prob_loyal
        self.identity       = "wealthy"
        self.influence      = 0.5
        self.fake_accounts  = [accounts.Account(self)]  # wealthy always have at least one fake account
        self.proxy          = self.proxy + 0.1
        
        if self.num_shoes_want > 1:
            self.fake_accounts.append(accounts.Account(self))


    def buy_shoes(self, cap):
        self._buy_shoes(min(cap, self.num_shoes_want + 1 - self.shoes_acquired, self.env.num_shoes))
        if self.shoes_acquired > 0 : self.got_shoes = True


class InfluencerConsumer(AverageConsumer):
    def __init__(self, env):
        AverageConsumer.__init__(self, env)
        self.identity                 = "influencer"
        self.num_shoes_want           = 1
        self.main_account.has_loyalty = False    # to simplify invite only mechanism
        self.influence                = 1
        self.fake_accounts            = []       # influencers do not create fake accounts
        self.influence                = 0.5


class ResellerConsumer(Consumer):
    def __init__(self, env):
        Consumer.__init__(self, env)
        self.desire         = 0
        self.proxy          = normal(self.env.mean_desire, self.env.std_desire)
        self.num_shoes_want = 100
        self.money          = 100000
        self.has_loyalty    = random() < self.env.reseller_prob_loyal
        self.identity       = "reseller"
        self.influence      = 0.5
        self.authenticated_fakes = [accounts.Account(self) for _ in range(7)]     # 20 fake accounts total
        self.fake_accounts = self.authorized_fake_accounts + [accounts.Account(self) for _ in range(13)]