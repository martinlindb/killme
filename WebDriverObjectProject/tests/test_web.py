"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""
import pytest
from result import DuckDuckGoResultPage
from search import DuckDuckGoSearchPage

from selenium.webdriver import Chrome

@pytest.fixture
def browser():
  # Initialize ChromeDriver
  driver = Chrome()
  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)
  
  # Return the driver object at the end of setup
  yield driver
  
  # For cleanup, quit the driver
  driver.quit()
def test_basic_duckduckgo_search(browser):
  # Set up some test case data
  PHRASE = 'panda'
  search_page = DuckDuckGoSearchPage(browser)
  search_page.load()
  search_page.search(PHRASE)

  # Verify that results appear on the results page
  result_page = DuckDuckGoResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE