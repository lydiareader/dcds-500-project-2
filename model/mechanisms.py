import random
import pandas as pd

# basic lottery system
def run_lottery_no_gaming(consumers):
    selected = random.sample(consumers, 100)

    for person in selected:
        person.buy_shoes(cap = 2)

    return agents_to_df(consumers)


def run_first_come_no_gaming(consumers):
    
    sorted_consumers = sorted(consumers, key = lambda c: c.desire, reverse=True)

    for person in sorted_consumers:
        person.buy_shoes(cap = 2)
    
    return agents_to_df(consumers)


def agents_to_df(consumers):
    fields = [
            'abnormal_size',
            'desire',
            'num_shoes_want',
            'money',
            'identity',
            'has_loyalty',
            'shoes_acquired'
            ]                
    return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in consumers])