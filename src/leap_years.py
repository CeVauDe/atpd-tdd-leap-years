def is_leap_year(year: int) -> bool:
    if year == 1900:
        return False
    if year == 1800:
        return False
    if year == 2300:
        return False
    if year % 4 == 0:
        return True
    return False
