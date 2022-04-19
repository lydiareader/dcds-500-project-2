# environment for simulation
import consumer
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

        # consumer types
        self.average_consumers    = [consumer.AverageConsumer(self) for _ in range(num_average)]
        self.abnormal_consumers   = [consumer.AbnormalConsumer(self) for _ in range(num_abnormal)]
        self.special_consumers    = [consumer.SpecialConsumer(self) for _ in range(num_special)]
        self.wealthy_consumers    = [consumer.WealthyConsumer(self) for _ in range(num_wealthy)]
        self.influencer_consumers = [consumer.InfluencerConsumer(self) for _ in range(num_influencers)]
        self.reseller_consumers   = [consumer.ResellerConsumer(self) for _ in range(num_resellers)]
        self.consumers = self.average_consumers + self.abnormal_consumers + self.special_consumers + self.wealthy_consumers + self.influencer_consumers + self.reseller_consumers

        self.fake_resellers = [consumer.ResellerConsumer(self) for _ in range(num_resellers * 20)]
        self.gaming_consumers = self.consumers + self.fake_resellers
        self.fake_resellers_firstcome = [consumer.ResellerConsumer(self) for _ in range(num_resellers * 5)]
        self.gaming_consumers_firstcome = self.consumers + self.fake_resellers_firstcome

        self.loyal_consumers = [person for person in self.consumers if person.has_loyalty]
        self.fake_loyal_consumer  = [consumer.ResellerConsumer(self) for _ in range(num_resellers * 7)]
        self.gaming_loyal_consumers = self.consumers + self.fake_loyal_consumer

        self.fake_resellers_auth = [consumer.ResellerConsumer(self) for _ in range(num_resellers * 7 ) ]
        self.gaming_consumers_auth = self.consumers + self.fake_resellers_auth

    def restock(self, num_shoes):
        self.num_shoes = num_shoes
        for person in self.consumers:
            person.reset()
        for person in self.fake_loyal_consumer:
            person.reset()
        for person in self.fake_resellers:
            person.reset()
        for person in self.fake_resellers_firstcome:
            person.reset()
        for person in self.fake_resellers_auth:
            person.reset()
    
    def restock_without_reset(self, num_shoes):
        self.num_shoes = num_shoes


    def run_invitation_no_gaming(self):
        selected = self.influencer_consumers + sample(self.loyal_consumers, 500)

        for person in selected:
            person.buy_shoes(cap = 2)

    def run_invitation_with_gaming(self):
        selected = self.influencer_consumers + sample(self.gaming_loyal_consumers,500)

        for person in selected:
            person.buy_shoes(cap = 2)

    def run_first_come_no_gaming(self):
        sorted_consumers = sorted(self.consumers, key = lambda c: c.desire, reverse=True)

        for person in sorted_consumers:
            person.buy_shoes(cap = 2)

    def run_first_come_with_gaming(self, cap = 2):
        sorted_consumers = sorted(self.gaming_consumers_firstcome, key = lambda c: c.proxy, reverse=True)
        
        for person in sorted_consumers:
            person.buy_shoes(cap = cap)

    def run_lottery_no_gaming(self, cap = 2):
        selected = sample(self.consumers, 1000)

        for person in selected:
            person.buy_shoes(cap = cap)

    def run_lottery_with_gaming(self, cap = 2):
        selected = sample(self.gaming_consumers, 1000)

        for person in selected:
            person.buy_shoes(cap = cap)

    def run_lottery_with_gaming_auth(self, cap = 2):
        selected = sample(self.gaming_consumers_auth, 1000)

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


    def get_fake_df(self):
        fields = [
                'abnormal_size',
                'desire',
                'num_shoes_want',
                'money',
                'identity',
                'has_loyalty',
                'influence',
                'shoes_acquired',
                'got_shoes'
                ]                
        return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in self.gaming_consumers])

    def get_fake_df_firstcome(self):
        fields = [
                'abnormal_size',
                'desire',
                'num_shoes_want',
                'money',
                'identity',
                'has_loyalty',
                'influence',
                'shoes_acquired',
                'got_shoes'
                ]                
        return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in self.gaming_consumers_firstcome])

    def get_fake_df_loyal(self):
        fields = [
                'abnormal_size',
                'desire',
                'num_shoes_want',
                'money',
                'identity',
                'has_loyalty',
                'influence',
                'shoes_acquired',
                'got_shoes'
                ]                
        return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in self.gaming_loyal_consumers])
    
    def get_fake_df_auth(self):
        fields = [
                'abnormal_size',
                'desire',
                'num_shoes_want',
                'money',
                'identity',
                'has_loyalty',
                'influence',
                'shoes_acquired',
                'got_shoes'
                ]                
        return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in self.gaming_consumers_auth])

    def get_real_fake_df(self):
        fakers = self.fake_resellers_auth + self.fake_loyal_consumer + self.fake_resellers_firstcome + self.fake_resellers
        consumer_set = self.consumers + fakers
        fields = [
                'abnormal_size',
                'desire',
                'num_shoes_want',
                'money',
                'identity',
                'has_loyalty',
                'influence',
                'shoes_acquired',
                'got_shoes'
                ]                
        return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in consumer_set]) 