import random
import pandas as pd

# basic lottery system
def run_lottery_no_gaming(consumers):
    selected = random.sample(consumers, 100)

    for person in selected:
        person.buy_shoes(cap = 2)

    fields = ['desire', 'identity', 'shoes_acquired']
    return pd.DataFrame([{field: getattr(person, field) for field in fields} for person in consumers])