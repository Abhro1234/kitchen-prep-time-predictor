def enrich_signals(data):

    queue = data["orders_in_queue"]

    if queue < 5:
        rush = "Low"
    elif queue < 15:
        rush = "Medium"
    else:
        rush = "High"

    data["rush_level"] = rush

    return data