import random

def predict_kpt(data):

    base = data["avg_prep_time"]

    load_factor = data["orders_in_queue"] * 1.8

    peak_factor = 8 if data["peak_hour"] else 0

    weekend_factor = 5 if data["weekend"] else 0

    noise = random.uniform(-2, 2)

    prep_time = base + load_factor + peak_factor + weekend_factor + noise

    prep_time = round(prep_time, 2)

    if prep_time < 20:
        load = "Low"
        confidence = 95
    elif prep_time < 40:
        load = "Medium"
        confidence = 90
    else:
        load = "High"
        confidence = 85

    return {
        "prep_time": prep_time,
        "kitchen_load": load,
        "confidence": confidence
    }