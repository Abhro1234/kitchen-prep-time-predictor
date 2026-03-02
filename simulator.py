import random

def simulate():

    return {
        "orders_in_queue": random.randint(1, 25),
        "avg_prep_time": random.randint(10, 25),
        "peak_hour": random.choice([True, False]),
        "weekend": random.choice([True, False])
    }