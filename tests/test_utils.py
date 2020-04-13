from instapy import time_util
from instapy import util
from datetime import datetime


def test_get_time():
    labels = ["this_hour", "this_minute", "today"]
    results = time_util.get_time(labels)
    date = datetime.now()
    assert results == [date.strftime("%H"), date.strftime("%M"), date.strftime("%Y-%m-%d")]


def test_username_url_to_username():
    url = "https://www.instagram.com/test_username/rest_of_url"
    result = util.username_url_to_username(url)
    assert result == "test_username"


def test_format_number():
    number = "3.2k"
    assert util.format_number(number) == 3200


def test_deform_emojis():
    emoji = "🤡 wow!"
    new_text, emojiless_text = util.deform_emojis(emoji)
    assert new_text == " (clown face) wow!"
    assert emojiless_text == " wow!"
