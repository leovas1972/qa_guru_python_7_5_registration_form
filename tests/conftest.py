import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.set_value_by_js = True
    browser.config.with_(click_by_js=True)