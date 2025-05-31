import csv
import pytest
from tests.keywords import KeywordDriven
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Enable incognito mode

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def read_keywords(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def test_keyword_execution(driver):
    keywords = read_keywords('data/keywords.csv')
    framework = KeywordDriven(driver)

    for step in keywords:
        keyword = step['Keyword']
        arg1 = step.get('Argument1')
        arg2 = step.get('Argument2')
        arg3 = step.get('Argument3')

        # Dynamically execute the method based on the keyword
        method = getattr(framework, keyword)
        if arg3:
            method(arg1, arg2, arg3)
        elif arg2 and not arg3:
            method(arg1, arg2)
        elif arg1 and not arg2:
            method(arg1)
        else:
            method()
