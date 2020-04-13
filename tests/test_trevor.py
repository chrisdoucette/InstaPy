from instapy import util


def test_remove_extra_spaces():
    text = "This has    extra   spaces."
    assert util.remove_extra_spaces(text) == "This has extra spaces."
