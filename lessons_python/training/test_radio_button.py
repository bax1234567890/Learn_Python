from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver (assuming Chrome)
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("http://test.rubywatir.com/radios.php")

    # Locate all radio buttons; assuming they share the same name attribute or located similarly
    # This page has radio buttons under different names. They can be grouped by the name attribute or by tag
    radio_buttons = driver.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')

    # Iterate over each radio button and click on it
    for index, button in enumerate(radio_buttons):
        if not button.is_selected():
            button.click()
            time.sleep(1)  # Sleep for 1 second to see the selection (optional, for visual confirmation)
            print(f"Radio button {index + 1} selected.")

            # Optionally, verify that the radio button is selected
            assert button.is_selected(), f"Radio button {index + 1} should be selected but isn't."

finally:
    # Close the browser after a delay
    time.sleep(2)  # Wait 2 seconds to observe the last selection
    driver.quit()

