from selenium import webdriver

driver = webdriver.Chrome("C:\sheldon\webscraping\chromedriver.exe")
driver.fullscreen_window()

driver.get("https://www.google.com")

elements = driver.find_elements_by_tag_name("a")
print(elements)
for element in elements:
    if "Images" == element.text:
        element.click()
        # driver.quit()
