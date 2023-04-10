from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as un
from selenium.common.exceptions import NoSuchElementException


class Bot:

    def __init__(self):
        chrome_options = un.ChromeOptions()
        chrome_options.add_argument('--enable-javascript')
        self.driver = un.Chrome(executable_path='/chromedriver')
        time.sleep(2)
        self.DEBUG = True
        self.cities = []


    def get_cities(self):
        self.driver.get('https://www.slixa.com/')
        cities = self.driver.find_elements(By.XPATH, '//div[@class="bigger"]//following-sibling::ul[@class="clearfix category-list"]//a')
        for city in cities:
            self.cities.append(city.get_attribute("href"))


    def get_profiles(self, url:str):

        page = 0
        while True:
            page += 1
            self.driver.get(f'{url}{page}/')
            try:
                self.driver.find_element(By.XPATH, "//h1[@class='cover-title' and contains(text(), 'OOPS!')]")
                break
            except NoSuchElementException:
                profiles1 = self.driver.find_elements(By.XPATH, '//ul[@id="abba-list"]//li[contains(@data-category, "category-escorts") and contains(@class, "city")]//*[@class="abba-click-link"]')
                profiles2 = self.driver.find_elements(By.XPATH, '//div[@class="span6 listing"]//i/a[@class="profile-link"]')
                profiles = profiles1 + profiles2

                for p in profiles:
                    self.profiles.append(p.get_attribute("href"))
