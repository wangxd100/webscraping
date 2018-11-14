from selenium import webdriver
import time
import uuid

driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
driver.get("https://www.baidu.com")
# driver.fullscreen_window()
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("i am makeing a screen shot!!!")
driver.save_screenshot(str(uuid.uuid4()) + ".png")

time.sleep(2)
driver.quit()