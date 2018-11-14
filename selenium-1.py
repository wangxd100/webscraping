# selenium >> pip install selenium
import time
from selenium import webdriver

# download Chrome Driver first
driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
# driver.fullscreen_window()

# ######### Test <a> click ##########
# driver.get("https://www.amazon.com")
# driver.find_element_by_id("nav-your-amazon").click()

# ######### Test Textbox ############
driver.get("https://www.google.com")
driver.maximize_window()

driver.find_element_by_link_text("Gmail").click()
driver.back()
driver.find_element_by_name("q").send_keys("mcps\n")
time.sleep(5)
driver.quit()






