'''Selenium 4 offers a new way of locating elements by using natural language terms such as
“above”, “below”, “left of”, “right of”, and “near”.
 This article describes how to use the new Relative Locators.'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Chrome()
driver.get("https://automationbookstore.dev/")
driver.maximize_window()
time.sleep(3)
book1 = driver.find_element(By.ID,"pid1_title")
book6 = driver.find_element(By.ID,"pid6_title")
book3 = driver.find_element(By.ID,"pid3_title")
driver.find_element(locate_with(By.TAG_NAME,"h2").below(book1).to_left_of(book6)).click()
#driver.find_element(locate_with(By.TAG_NAME,"input").above(book1)).send_keys("hi")
driver.find_element(locate_with(By.TAG_NAME,"h2").to_right_of(book1).above(book6)).click()
time.sleep(5)
driver.close()

