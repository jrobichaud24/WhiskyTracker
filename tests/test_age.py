from datetime import date

from whiskytracker.age import calculate_age


def test_age_on_birthday():
    assert calculate_age(date(2000, 1, 1), date(2020, 1, 1)) == 20


def test_age_before_birthday():
    # bottled date is before the distilled date's anniversary
    assert calculate_age(date(2000, 6, 1), date(2020, 5, 31)) == 19
