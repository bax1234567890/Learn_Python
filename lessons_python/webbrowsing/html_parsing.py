#  pip install beautifulsoup4

import bs4
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def getRocketshipsJobs(productUrl):
    res = requests.get(productUrl)  # Navigate to website
    res.raise_for_status()  # Raise for staus. If there is error we can see it

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#app > div > div.job-search-list > div > div.section-header-row > h2')

    return elems[0].text.strip()

jobs = getRocketshipsJobs('https://rocketships.io/')
print("The job is " + jobs)



#----#---------#----------#

def getAmazonPrice(productURL):
    res = requests.get('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/') # Download the page
    res.raise_for_status() # Raise for staus. If there is error we can see it

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # elems = soup.select('#page > div.wrapper > main > div > h1')
    # return elems[0].text.strip()

# stripprice = getAmazonPrice('https://account.dji.com/login?appId=flysafe-websdite-be&locale=en_US')
# price('The price is ' + price)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def getAmazonPrice(productURL):
#     driver = webdriver.Chrome()  # Path to your chromedriver
#     driver.get(productURL)
#
#     # Optional: login or wait for page to load
#     # driver.find_element_by_id('login').click()
#
#     elems = driver.find_elements(By.XPATH, "//span[@id='taxInclusiveMessage']")
#     # price = elems[0].text if elems else "No price found."
#     driver.quit()
#     return elems
#
# # Example usage
# price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
# print('The price is ' + price)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def check_for_price():
#     driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or specify the path
#     try:
#         driver.get("https://www.example.com")  # Replace with your target URL
#
#         elems = driver.find_elements(By.XPATH, "//*[='text,'$24.49']")
#         if elems:
#             for elem in elems:
#                 text = elem.text.strip()
#                 print("Found text:", text)
#
#                 if '$' in text:
#                     print("Price found:", text)
#                 else:
#                     print("No price found in the element.")
#         else:
#             print("No elements found with the specified ID.")
#     finally:
#         driver.quit()
#
# # Run the function to check for price
# check_for_price()
