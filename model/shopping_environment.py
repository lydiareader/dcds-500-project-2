# environment for simulation
import consumer
import accounts
from random import sample
import pandas as pd

class ShoppingEnvironment():
    def __init__(self, mean_desire, std_desire, desire_threshold, average_mean_money, average_std_money, \
                    rich_mean_money, rich_std_money, average_prob_loyal, rich_prob_loyal, reseller_prob_loyal, num_shoes, price, \
                        num_average, num_abnormal, num_special, num_wealthy, num_influencers, num_resellers):

        self.mean_desire            = mean_desire
        self.std_desire             = std_desire
        self.desire_threshold       = desire_threshold
        self.average_mean_money     = average_mean_money
        self.average_std_money      = average_std_money
        self.rich_mean_money        = rich_mean_money
        self.rich_std_money         = rich_std_money
        self.average_prob_loyal     = average_prob_loyal
        self.rich_prob_loyal        = rich_prob_loyal
        self.reseller_prob_loyal    = reseller_prob_loyal
        self.num_shoes              = num_shoes
        self.price                  = price
        self.num_resellers          = num_resellers

        # consumer types
        self.average_consumers    = [consumer.AverageConsumer(self) for _ in range(num_average)]
        self.abnormal_consumers   = [consumer.AbnormalConsumer(self) for _ in range(num_abnormal)]
        self.special_consumers    = [consumer.SpecialConsumer(self) for _ in range(num_special)]
        self.wealthy_consumers    = [consumer.WealthyConsumer(self) for _ in range(num_wealthy)]
        self.influencer_consumers = [consumer.InfluencerConsumer(self) for _ in range(num_influencers)]
        self.reseller_consumers   = [consumer.ResellerConsumer(self) for _ in range(num_resellers)]
        self.consumers = self.average_consumers + self.abnormal_consumers + self.special_consumers + self.wealthy_consumers + self.influencer_consumers + self.reseller_consumers

        self.main_accounts = [person.main_account for person in self.consumers]
        self.fake_accounts = []
        for person in self.consumers:
            self.fake_accounts = self.fake_accounts + person.fake_accounts


        self.loyal_main_accounts = [account for account in self.main_accounts if account.has_loyalty]
        self.loyal_fake_accounts = [account for account in self.fake_accounts if account.has_loyalty]


    def restock(self, num_shoes):
        self.num_shoes = num_shoes
        for person in self.consumers:
            person.reset()
    

    def restock_without_reset(self, num_shoes):
        self.num_shoes = num_shoes


    ## No Gaming ----------------------------------------------------------------------------------
    def run_lottery_no_gaming(self, cap = 2):
        selected = sample(self.main_accounts, 1000)

        for account in selected:
            account.person.buy_shoes(cap = cap)
            
    
    def run_first_come_no_gaming(self, cap = 2):
        sorted_consumers = sorted(self.consumers, key = lambda c: c.desire, reverse=True)

        for person in sorted_consumers:
            person.buy_shoes(cap = cap)

    
    def run_invitation_no_gaming(self, cap = 2):
        for person in self.influencer_consumers:
            person.buy_shoes(cap = cap)
        
        selected = sample(self.loyal_main_accounts, 500)
        for account in selected:
            account.person.buy_shoes(cap = cap)


    ## No Gaming ----------------------------------------------------------------------------------
    def run_lottery_with_gaming(self, cap = 2):
        selected = sample(self.fake_accounts + self.main_accounts, 1000)

        for account in selected:
            account.person.buy_shoes(cap = cap)

    
    def run_invitation_with_gaming(self, cap = 2):
        for person in self.influencer_consumers:
            person.buy_shoes(cap = cap)
        
        selected = sample(self.loyal_fake_accounts, 500)
        for account in selected:
            account.person.buy_shoes(cap = cap)


    def run_first_come_with_gaming(self, cap = 2):
        num_fakes = self.num_resellers * 5
        gaming_consumers = self.consumers + sample(self.fake_resellers, num_fakes)
        sorted_consumers = sorted(gaming_consumers, key = lambda c: c.proxy, reverse=True)
        
        for person in sorted_consumers:
            person.buy_shoes(cap = cap)


    ## Authentication ----------------------------------------------------------------------------------
    def run_lottery_with_gaming_auth(self, cap = 2):
        num_fakes = self.num_resellers * 7
        fakers = sample(self.fake_resellers, num_fakes)
        selected = sample(self.consumers + fakers, 1000)

        for person in selected:
            person.buy_shoes(cap = cap)


    def get_consumer_df(self):
        fields = [
                'abnormal_size',
                'desire',
                'num_shoes_want',
                'money',
                'identity',
                'has_loyalty',
                'influence',
                'shoes_acquired'
                ]                
        return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in self.consumers])