import consumer
from shopping_environment import ShoppingEnvironment


env = ShoppingEnvironment(
    desire_threshold = 0.7,
    average_mean_money = 250,
    average_std_money = 15,
    rich_mean_money = 1000,
    average_prob_loyal = 0.5,
    rich_prob_loyal = 0.8,
    reseller_prob_loyal = 0.9
)
average_consumer = consumer.AverageConsumer(env)
average_consumer.printdesire()