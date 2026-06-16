def rescue_priority(
        severity,
        people,
        distance):

    score = (
        severity * 5 +
        people * 2 -
        distance
    )

    return score


if __name__ == "__main__":

    priority = rescue_priority(
        severity=9,
        people=50,
        distance=10
    )

    print(priority)