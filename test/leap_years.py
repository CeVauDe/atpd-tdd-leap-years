from src.leap_years import is_leap_year


class TestShouldLeapYear:

    def test_leap_year(self):
        assert is_leap_year() == False
