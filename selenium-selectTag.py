from selenium import webdriver
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
driver.get("https://www.timeanddate.com/")
driver.maximize_window()
# driver.fullscreen_window()
elements = driver.find_element_by_id("month")
m = Select(elements)
m.select_by_value("3")
# m.select_by_visible_text("December")

countyElement = driver.find_element_by_id("country")
c = Select(countyElement)
c.select_by_value("27")

driver.find_element_by_xpath("//input[@value='View Calendar']").click()
time.sleep(2)
driver.quit()


