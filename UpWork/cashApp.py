from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pyzbar.pyzbar import decode
from PIL import Image
import time


# Function to click and fill a field with "123rdg"
def click_and_fill_field(driver, field_locator):
    # Navigate to the web page with the form
    driver.get('URL_OF_YOUR_WEB_PAGE')

    # Find the field and click it
    field = driver.find_element(By.NAME, field_locator)
    field.click()

    # Fill the field with "123rdg"
    field.send_keys("123rdg")


# Function to capture and decode QR code
def capture_and_decode_qr(screenshot_path):
    # Load the screenshot
    image = Image.open(screenshot_path)

    # Decode the QR code
    qr_codes = decode(image)

    # Extract the URL from the QR code
    qr_url = None
    for qr in qr_codes:
        qr_url = qr.data.decode('utf-8')
        break

    if qr_url:
        print(f"QR Code URL: {qr_url}")
        return qr_url
    else:
        print("No QR code found")
        return None


# Set up Selenium
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Call the function with the locator of the field you want to fill
click_and_fill_field(driver, 'FIELD_NAME')

# Path to the screenshot
screenshot_path = '/Users/ionbota/Documents/Screenshot 2024-06-11 at 4.30.08 PM.png'

# Capture and decode QR code
qr_url = capture_and_decode_qr(screenshot_path)

# Navigate to the QR code URL if found
if qr_url:
    driver.get(qr_url)

# Wait for a few seconds to see the result (optional)
time.sleep(5)

# Close the browser
driver.quit()
