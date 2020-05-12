import pytest
from instapy import util
from instapy import InstaPy
from instapy import like_util


def test_remove_extra_spaces():
    text = "This has    extra   spaces."
    assert util.remove_extra_spaces(text) == "This has extra spaces."


@pytest.mark.skip(reason="github actions not working properly with selenium web drivers")
def test_get_user_links():
    session = InstaPy(username='trevorsfirstinsta', password='NewTest1234!', headless_browser=False)
    session.login()
    test_amount = 5
    results = like_util.get_links_for_username(session.browser, session.username, 'cristiano',
                                               amount=test_amount, logger=session.logger, logfolder=session.logfolder,
                                               randomize=False, media=None, taggedImages=False)
    assert len(results) == test_amount


@pytest.mark.skip(reason="github actions not working properly with selenium web drivers")
def test_get_locations_links():
    # launches InstaPy
    session = InstaPy(username='trevorsfirstinsta', password='NewTest1234!', headless_browser=False)
    session.login()
    test_amount = 5
    test_location = ['212988663']
    results = like_util.get_links_for_location(browser=session.browser, location=test_location, amount=test_amount,
                                               logger=session.logger,skip_top_posts=False)
    assert len(results) == test_amount
