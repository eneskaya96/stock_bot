from selenium import webdriver


class SeleniumService:

    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def open_yapi_kredi(self):
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

        self.driver.get("https://www.yapikredi.com.tr/")
        return self.driver
