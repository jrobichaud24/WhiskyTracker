from __future__ import annotations

from datetime import date


def calculate_age(distilled_date: date, bottled_date: date | None = None) -> int:
    """Calculate age of whisky in whole years.

    Args:
        distilled_date: When the whisky was distilled.
        bottled_date: When the whisky was bottled. Uses today's date when None.

    Returns:
        The number of full years between the two dates.

    The previous implementation used a simple year difference which
    produced an off-by-one error when the bottled date had not yet
    reached the anniversary of the distilled date. This implementation
    subtracts one year in those cases to provide the correct age.
    """
    if bottled_date is None:
        bottled_date = date.today()

    age = bottled_date.year - distilled_date.year
    if (bottled_date.month, bottled_date.day) < (distilled_date.month, distilled_date.day):
        age -= 1
    return age
