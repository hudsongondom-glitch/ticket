import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from celsius import celsius_to_fahrenheit


class TestNormalValues:
    def test_room_temperature(self):
        assert celsius_to_fahrenheit(20) == pytest.approx(68.0)

    def test_body_temperature(self):
        assert celsius_to_fahrenheit(37) == pytest.approx(98.6)

    def test_ten_degrees(self):
        assert celsius_to_fahrenheit(10) == pytest.approx(50.0)

    def test_fifty_degrees(self):
        assert celsius_to_fahrenheit(50) == pytest.approx(122.0)

    def test_hundred_degrees(self):
        assert celsius_to_fahrenheit(100) == pytest.approx(212.0)


class TestZero:
    def test_zero_celsius_is_freezing_point(self):
        assert celsius_to_fahrenheit(0) == pytest.approx(32.0)

    def test_zero_returns_float_compatible_value(self):
        assert celsius_to_fahrenheit(0) == 32


class TestBoilingAndFreezing:
    def test_freezing_point_of_water(self):
        assert celsius_to_fahrenheit(0) == pytest.approx(32.0)

    def test_boiling_point_of_water(self):
        assert celsius_to_fahrenheit(100) == pytest.approx(212.0)


class TestNegativeValues:
    def test_negative_ten(self):
        assert celsius_to_fahrenheit(-10) == pytest.approx(14.0)

    def test_negative_forty_is_equal_in_both_scales(self):
        assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)

    def test_negative_one(self):
        assert celsius_to_fahrenheit(-1) == pytest.approx(30.2)

    def test_negative_two_hundred(self):
        assert celsius_to_fahrenheit(-200) == pytest.approx(-328.0)


class TestAbsoluteZero:
    def test_absolute_zero(self):
        assert celsius_to_fahrenheit(-273.15) == pytest.approx(-459.67)

    def test_below_absolute_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            celsius_to_fahrenheit(-300)

    def test_just_below_absolute_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            celsius_to_fahrenheit(-273.16)


class TestFractionalValues:
    def test_fractional_positive(self):
        assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)

    def test_fractional_negative(self):
        assert celsius_to_fahrenheit(-15.5) == pytest.approx(4.1)

    def test_small_fraction(self):
        assert celsius_to_fahrenheit(0.1) == pytest.approx(32.18)

    def test_repeating_fraction(self):
        assert celsius_to_fahrenheit(1 / 3) == pytest.approx(32.6)


class TestIncreasingBehaviour:
    def test_conversion_is_monotonically_increasing(self):
        values = [-50, -10, 0, 10, 25, 37, 100]
        results = [celsius_to_fahrenheit(v) for v in values]
        assert results == sorted(results)

    def test_higher_celsius_gives_higher_fahrenheit(self):
        assert celsius_to_fahrenheit(30) > celsius_to_fahrenheit(20)

    def test_one_degree_celsius_difference_is_1_8_fahrenheit(self):
        diff = celsius_to_fahrenheit(11) - celsius_to_fahrenheit(10)
        assert diff == pytest.approx(1.8)


class TestInvalidInput:
    def test_string_input_raises_type_error(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit("20")

    def test_none_input_raises_type_error(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit(None)

    def test_list_input_raises_type_error(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit([20])

    def test_dict_input_raises_type_error(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit({"value": 20})

    def test_boolean_input_raises_type_error(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit(True)


class TestBoundaryCases:
    def test_large_positive_value(self):
        assert celsius_to_fahrenheit(1000) == pytest.approx(1832.0)

    def test_value_just_above_absolute_zero(self):
        assert celsius_to_fahrenheit(-273.14) == pytest.approx(-459.652)

    def test_very_small_negative_fraction(self):
        assert celsius_to_fahrenheit(-0.0001) == pytest.approx(31.99982)
