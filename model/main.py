import consumer
from shopping_environment import ShoppingEnvironment

# parameters
num_shoes        = 100

# number of each consumer type
num_average     = 900
num_abnormal    = 100
num_special     = 25
num_wealthy     = 100
num_influencers = 50
num_resellers   = 25

# initialize environment
env = ShoppingEnvironment(
    mean_desire = 0.5,
    std_desire = 0.2,
    desire_threshold = 0.7,
    average_mean_money = 250,
    average_std_money = 15,
    rich_mean_money = 1000,
    rich_std_money = 250,
    average_prob_loyal = 0.5,
    rich_prob_loyal = 0.8,
    reseller_prob_loyal = 0.9
)

# create consumers
average_consumers    = [consumer.AverageConsumer(env) for _ in range(num_average)]
abnormal_consumers   = [consumer.AbnormalConsumer(env) for _ in range(num_abnormal)]
special_consumers    = [consumer.SpecialConsumer(env) for _ in range(num_special)]
wealthy_consumers    = [consumer.WealthyConsumer(env) for _ in range(num_wealthy)]
influencer_consumers = [consumer.InfluencerConsumer(env) for _ in range(num_influencers)]
reseller_consumers   = [consumer.ResellerConsumer(env) for _ in range(num_resellers)]


