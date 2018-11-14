from selenium import webdriver
import time

driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
driver.get("https://www.google.com")
# driver.fullscreen_window()
driver.maximize_window()
time.sleep(2)

# driver.minimize_window()

# title
print(driver.title)

# get current url
print(driver.current_url)

# refresh
driver.refresh()


# another url
driver.get("https://www.youtube.com")
time.sleep(1)

# go back
driver.back()
time.sleep(1)

# forward
driver.forward()

print(driver.page_source)
# close and quit
# close current tab
# driver.close()
# close all opened browser by program
driver.quit()
