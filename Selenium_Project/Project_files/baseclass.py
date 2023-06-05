from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Base:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')

    chrome_path = Service('/Users/amirantevzadze/Documents/development/chromedriver')

    driver = webdriver.Chrome(service=chrome_path, options=chrome_options)
    driver.implicitly_wait(20)
    driver.get('https://www.ebay.com/')

    def item_search(self, text):
        self.driver.find_element(By.XPATH, '//*[@id="gh-ac"]').send_keys(text)
        self.driver.find_element(By.ID, 'gh-btn').click()

    def buy_it_now(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='BIN=1']").click()

    def close_window(self):
        return self.driver.close()

    def next_page(self):
        return self.driver.find_element(By.CLASS_NAME, 'pagination__next').click()

    def verifylink(self, locator, text=str):
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_all_elements_located((locator, text)))

    def switch_window(self, num):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[num])

    def open_new_tab(self):
        return self.driver.execute_script("window.open('');")

    def clearSearch(self):
        self.driver.find_element(By.XPATH, '//*[@id="gh-ac"]').clear()
