from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from options import Driver

web_driver = Driver()

class Base:


    def close_window(self):
        return web_driver.driver.close()

    def VerifylinkPresence(self, locator, text=str):
        WebDriverWait(web_driver.driver, 15).until(expected_conditions.presence_of_all_elements_located((locator, text)))


    def switch_window(self, num):
        all_windows = web_driver.driver.window_handles
        switch = web_driver.driver.switch_to.window(all_windows[num])
        return switch

    def switch_to_google_forms(self):
        sww = web_driver.driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfmSm8WTGkHgh7MvfO6wy3SwsNNWpJ5ubQ51nh8ESO8qD5jcg/viewform?usp=sf_link')
        return sww

    def open_new_tab(self):
        return web_driver.driver.execute_script("window.open('');")

    def clearSearch(self):
        web_driver.driver.find_element(By.XPATH, '//*[@id="gh-ac"]').clear()