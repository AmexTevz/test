from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Driver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')

    chrome_path = Service('/Users/amirantevzadze/Documents/development/chromedriver')

    driver = webdriver.Chrome(service=chrome_path, options=chrome_options)
    driver.implicitly_wait(20)