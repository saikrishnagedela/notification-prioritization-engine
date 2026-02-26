def apply_rules(notification):
    if notification.priority_hint == "high":
        return 8
    elif notification.priority_hint == "low":
        return 3
    return 5