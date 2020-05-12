import pytest

from instapy import util
from instapy import InstaPy
from datetime import datetime
from instapy import relationship_tools
from instapy import time_util


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


@pytest.mark.skip(reason="github actions not working properly with selenium webdrivers")
def test_get_followers_by_ratio():
    instagram_username = 'netsud0'
    instagram_password = 'Comp490Test!'

    session = InstaPy(username=instagram_username,
                      password=instagram_password,
                      headless_browser=False)

    session.login()
    followers = relationship_tools.get_followers_by_ratio\
        (session.browser, instagram_username, session.relationship_data, 1, session.logger, session.logfolder)
    assert len(followers) == 1
    session.browser.close()


@pytest.mark.skip(reason="github actions not working properly with selenium webdrivers")
def test_automated_scroll():
    instagram_username = 'netsud0'
    instagram_password = 'Comp490Test!'

    session = InstaPy(username=instagram_username,
                      password=instagram_password,
                      headless_browser=False)

    session.login()
    util.web_address_navigator(session.browser, 'https://www.instagram.com/instagram/')
    time_util.sleep(2)
    scroll_offset = session.browser.execute_script('return window.scrollY')
    assert scroll_offset > 0
    session.browser.close()
