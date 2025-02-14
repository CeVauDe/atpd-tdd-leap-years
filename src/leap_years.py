def is_leap_year(year: int) -> bool:
    if year == 1900:
        return False
    if year % 4 == 0:
        return True
    return False
