import pytest
from selene import browser

@pytest.fixture()
def set_window_size():
    browser.config.window_height = 1060
    browser.config.window_width = 1440

@pytest.fixture()
def set_browser_name():
    browser.config.browser_name = 'chrome'

@pytest.fixture()
def open_demoqa(set_browser_name, set_window_size):
    browser.open('https://demoqa.com/automation-practice-form')