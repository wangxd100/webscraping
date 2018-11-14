
from selenium import webdriver

driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
driver.fullscreen_window()

driver.get("https://www.douban.com/")
driver.find_element_by_class_name("lnk-movie").click()

