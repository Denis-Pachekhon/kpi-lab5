from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def test():
    searchText = 'chorts'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(20)

    driver.get('https://www.asos.com/')
    driver.find_elements_by_css_selector('#chrome-search')[0].send_keys(searchText)
    driver.find_elements_by_css_selector('#chrome-search')[0].send_keys(Keys.ENTER)


    receivedText = driver.find_elements_by_css_selector('.vp-JnyG')[0].text.lower()

    print(receivedText)
    assert receivedText == "\"" + searchText + "\"", 'Error test'

    # python -m pytest test.py 