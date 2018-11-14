from selenium import webdriver
import time


driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
# driver.fullscreen_window()

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/a[2]").click()


