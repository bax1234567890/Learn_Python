import unittest



# Reverse a String
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"


# Find Duplicates in a List
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

print(find_duplicates([1, 2, 3, 4, 4, 5, 6, 6]))  # Output: [4, 6]


# Writing a Unit Test with unittest
def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()


# Automating a Login with Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login(url, username, password):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(2)  # wait for the page to load

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    time.sleep(2)  # wait for login to process
    assert "Dashboard" in driver.title  # or another assertion to confirm login

    driver.quit()

login("http://example.com/login", "your_username", "your_password")



# Reading and Parsing a JSON File
import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

data = read_json('data.json')
print(data)


# Testing an API with requests
import requests

def test_api(url):
    response = requests.get(url)
    assert response.status_code == 200
    print(response.json())

test_api('https://jsonplaceholder.typicode.com/posts/1')


# File Manipulation
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

file_content = read_file('example.txt')
print(file_content)
write_file('example_copy.txt', file_content)



# Writing a Test Case with pytest
# test_math_functions.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

# To run this test, use the command: pytest test_math_functions.py


