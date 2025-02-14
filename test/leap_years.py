import pytest

from src.leap_years import is_leap_year


class TestShouldLeapYear:

    @pytest.mark.parametrize(
        "year,expectation", [(2001, False), (2003, False), (1993, False), (1996, True)]
    )
    def test_leap_year(self, year: int, expectation: bool):
        assert is_leap_year(year) == expectation
