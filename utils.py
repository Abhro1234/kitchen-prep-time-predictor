def calculate_load(prep_time):

    if prep_time < 20:
        return "Low"
    elif prep_time < 40:
        return "Medium"
    else:
        return "High"