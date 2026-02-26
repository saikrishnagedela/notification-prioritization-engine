def decide(score):
    if score > 7:
        return "NOW"
    elif score >= 4:
        return "LATER"
    return "NEVER"