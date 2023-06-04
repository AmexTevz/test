from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')

chrome_path = Service('/Users/amirantevzadze/Documents/development/chromedriver')

driver = webdriver.Chrome(service=chrome_path,options=chrome_options)
driver.implicitly_wait(20)