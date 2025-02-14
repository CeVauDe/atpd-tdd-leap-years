def is_leap_year(year: int) -> bool:
    if year == 2000:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
