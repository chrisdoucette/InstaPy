from instapy.util import truncate_float


def test_truncate_float():
    number = 5.49
    precision = 1
    assert truncate_float(number, precision) == 5.4
