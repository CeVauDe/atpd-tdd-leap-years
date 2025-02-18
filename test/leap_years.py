import pytest

from src.leap_years import is_leap_year


class TestShouldLeapYear:

    @pytest.mark.parametrize(
        "year,expectation",
        [
            (2001, False),
            (2003, False),
            (1993, False),
            (1996, True),
            (1992, True),
            (1888, True),
            (1900, False),
            (1800, False),
            (2300, False),
            (2000, True),
            (1600, True),
            (2400, True),
        ],
    )
    def test_leap_year(self, year: int, expectation: bool):
        assert is_leap_year(year) == expectation
