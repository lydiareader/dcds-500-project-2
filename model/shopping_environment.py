# environment for simulation


class ShoppingEnvironment():
    def __init__(self, mean_desire, std_desire, desire_threshold, average_mean_money, average_std_money, \
                    rich_mean_money, rich_std_money, average_prob_loyal, rich_prob_loyal, reseller_prob_loyal, num_shoes, price):

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
        self.consumers              = []

    def restock(self, num_shoes):
        self.num_shoes = num_shoes
        for person in self.consumers:
            person.reset()