import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to USPS and search packege
browser = webdriver.Chrome()
browser.get('https://www.usps.com/')
element = browser.find_element(By.XPATH, "//*[@id='home-input']")
element.send_keys('123456789')
element.submit()
time.sleep(3)

browser.back()
browser.back()
time.sleep(3)

browser.forward()
time.sleep(3)

browser.refresh()
browser.refresh()
time.sleep(3)
# print(element.text)
browser.quit()


#---#---#---#---#---#---#---#---#---#---#---#---#---#

# Find text in page and print info from paragraph
# browser = webdriver.Chrome()
# browser.get('https://www.usps.com/')
# element = browser.find_element(By.XPATH,"//p[contains(text(), 'Forever')]")
# print(element.text)

#---#---#---#---#---#---#---#---#---#---#---#---#---#

# Setup WebDriver
# driver = webdriver.Chrome()  # Assuming chromedriver is in PATH or specified
#
# # Use a method properly
# driver.get("https://automatetheboringstuff.com/")  # Correctly using the .get() method of the driver
#
# # Example of finding an element (also a correct usage)
# element = driver.find_elements(By.XPATH, "//a[contains(text(),'Introduction')]")
# element.click()
# # elements = driver.find_element(By.CSS_SELECTOR, 'p')
# # len(element)
# print(element.text)
# time.sleep(5)
# # Close the WebDriver session properly
# driver.quit()


#---#---#---#---#---#---#---#---#---#---#---#---#---#
#
# driver = webdriver.Chrome()
# driver.get("https://automatetheboringstuff.com")
# elements = driver.find_elements(By.XPATH, "//li[contains(text(), 'Introduction')]")
# for e in elements:
#     print(e.text)
