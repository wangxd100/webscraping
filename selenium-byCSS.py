from selenium import webdriver
import time


driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
# driver.fullscreen_window()

driver.get("https://www.baidu.com")
driver.maximize_window()
driver.find_element_by_css_selector("#kw").send_keys("test\n")
