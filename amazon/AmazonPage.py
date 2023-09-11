from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService


class AmazonPage:
    def __init__(self):
        self.driver = None

    def open_amazon_home_page(self, url):
        if self.driver is None:
            driver_path = r'C:\Users\user\.cache\selenium\chromedriver\win32\114.0.5735.90\chromedriver.exe'
            chrome_service = ChromeService(executable_path=driver_path)
            self.driver = webdriver.Chrome(service=chrome_service)
        self.driver.get(url)

    def click_filter_button(self):
        filter_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='nav-left'])[2]"))
        )
        filter_button.click()

    def click_books_filter(self):
        books_item = self.driver.find_element(By.XPATH, "//option[text()='Books']")
        books_item.click()

    def type_value_in_input(self, value):
        search_input = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_input.clear()
        search_input.send_keys(value)
        search_input.send_keys(Keys.ENTER)

    def get_title_list(self):
        title_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div/div/h2//span"))
        )
        return [title.text for title in title_list]

    def get_author_list(self):
        author_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='a-row']"))
        )
        return [author.text for author in author_list]

    def get_price_list(self):
        price_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//span[@class='a-price-whole']"))
        )
        return [price.text for price in price_list]

    @staticmethod
    def get_filter_author_list(title_list):
        filter_author_list = []
        for title in title_list:
            if "by" in title:
                elements = title.split("by")
                if len(elements) > 1:
                    author = elements[1].strip()
                    filter_author_list.append(author)
        return filter_author_list

    def close_browser(self):
        if self.driver:
            self.driver.quit()
