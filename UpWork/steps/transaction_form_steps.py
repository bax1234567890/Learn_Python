# import time
# import cv2
# from behave import given, when, then
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from PIL import Image
#
# driver = None
#
# @given('I navigate to the transaction form page')
# def step_impl(context):
#     global driver
#     driver = webdriver.Chrome()
#     driver.get('https://auto.com')
#
#     # Wait for the page to load
#     time.sleep(5)
#
#     # Log in to the site
#     username_field = driver.find_element(By.NAME, 'Username')
#     password_field = driver.find_element(By.NAME, 'Password')
#     login_button = driver.find_element(By.NAME, 'Submit')  # Replace with the actual name or another locator for the login button if 'Submit' is not correct
#
#     # Enter credentials
#     username_field.send_keys('your_username')
#     password_field.send_keys('your_password')
#     login_button.click()
#
#     # Wait for the next page to load
#     time.sleep(5)
#
#    @when('I fill out the transaction form with cashtag, name, and email')
# def step_impl(context):
#     driver.find_element_by_xpath("//input[@id='cashtag']").send_keys('CASHTAG')
#     driver.find_element_by_xpath("//input[@id='name']").send_keys('Na,eCASHTAG')
#     driver.find_element_by_xpath("//input[@id='buyer_email']").send_keys('bota.ion.olege@example.com')
# #
# # @when('I submit the transaction form')
# # def step_impl(context):
# #     driver.find_element_by_name('submit').click()
# #
# # @then('a new window with a QR code appears')
# # def step_impl(context):
# #     # Switch to the new window
# #     driver.switch_to.window(driver.window_handles[1])
# #     time.sleep(5)  # Adjust sleep as necessary to ensure page loads completely
# #
# # @then('I scan the QR code')
# # def step_impl(context):
# #     # Screenshot the QR code
# #     qr_code_element = driver.find_element_by_xpath('XPATH_OF_QR_CODE_IMAGE')
# #     qr_code_element.screenshot('/path/to/qr_code.png')
# #
# #     # Decode the QR code
# #     qr_code_image = Image.open('/path/to/qr_code.png')
# #     decoded_qr_codes = decode(qr_code_image)
# #     context.qr_data = decoded_qr_codes[0].data.decode('utf-8')
# #
# # @then('I navigate to Cashapp with the scanned QR code')
# # def step_impl(context):
# #     # Here we assume you can use the QR data to navigate
# #     # This step depends on how Cashapp expects the QR code data to be provided
# #     # As a placeholder, just print the QR data
# #     print(context.qr_data)
# #
# # @then('I fill "For" with text from the previous page')
# # def step_impl(context):
# #     # Fill in "For" field in Cashapp
# #     # Placeholder action, need Cashapp interaction details
# #     pass
# #
# # @then('I fill "Price" with price from the previous page')
# # def step_impl(context):
# #     # Fill in "Price" field in Cashapp
# #     # Placeholder action, need Cashapp interaction details
# #     pass
# #
# # @then('I make the payment')
# # def step_impl(context):
# #     # Submit the payment in Cashapp
# #     # Placeholder action, need Cashapp interaction details
# #     pass
# #
# # @then('I close the browser')
# # def step_impl(context):
# #     global driver
# #     if driver:
# #         driver.quit()