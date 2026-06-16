def flood_probability(
        rainfall,
        river_level):

    if rainfall > 100 and river_level > 80:

        return 0.90

    if rainfall > 70:

        return 0.60

    return 0.20


def cyclone_probability(
        wind_speed):

    if wind_speed > 120:

        return 0.85

    if wind_speed > 80:

        return 0.55

    return 0.15


if __name__ == "__main__":

    print(
        flood_probability(
            120,
            85
        )
    )

    print(
        cyclone_probability(
            130
        )
    )