from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.yapikredi.com.tr/")

while 1:
    sleep(100)

#ele = driver.find_element('class="nav-item dropdown full-height item-center internet-subesi border-0 redList navList show"')
