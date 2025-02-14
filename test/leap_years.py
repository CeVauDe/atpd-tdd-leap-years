from src.leap_years import is_leap_year


class TestShouldLeapYear:

    def test_leap_year(self):
        assert is_leap_year(2001) == False
        assert is_leap_year(2003) == False
        assert is_leap_year(1993) == False
