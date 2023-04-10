from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as un
from selenium.common.exceptions import NoSuchElementException

class GetInfo:

    def __init__(self):
        chrome_options = un.ChromeOptions()
        chrome_options.add_argument('--enable-javascript')
        self.driver = un.Chrome(executable_path='/chromedriver')
        time.sleep(2)
        self.DEBUG = True

    def get_info(self, url: str):
        self.driver.get(url)
        self.name = None

        try:
            self.name = self.driver.find_element(By.XPATH, "//h1[@itemprop='name' and @class='cover-title']").text.strip()
        except NoSuchElementException:
            self.name = None

        if '/ca/' in self.driver.current_url:
            self.country = 'Canada'
        elif '/uk/' in self.driver.current_url:
            self.country = 'United Kingdom'
        elif '/au/' in self.driver.current_url:
            self.country = 'Australia'
        else:
            self.country = 'United States'

        self.city = None

        try:
            self.city = self.driver.find_element(By.XPATH, "//div[@class='current-location']/p").text.strip()
        except NoSuchElementException:
            try:
                self.city = self.driver.find_element(By.XPATH, "//*[@class='current-location must-travel']//a").text.strip()
            except NoSuchElementException:
                self.city = None

        self.email = None
        lst = []
        try:
            emails = self.driver.find_elements(By.XPATH, "//*[@data-contactmethod='email']")
            for email in emails:
                lst.append(email.get_attribute("data-contactdata"))
            self.email = ', '.join(set(lst))
        except NoSuchElementException:
            self.email = None

        self.phone = None
        lst = []
        try:
            phones = self.driver.find_elements(By.XPATH, "//*[@data-contactmethod='phone']")
            for phone in phones:
                lst.append(phone.get_attribute("data-contactdata"))
            self.phone = ', '.join(set(lst))
        except NoSuchElementException:
            self.email = None

        if self.DEBUG:
            print("Name:", self.name)
            print("Country:", self.country)
            print("City:", self.city)
            print("Email:", self.email)
            print("Phone:", self.phone)
