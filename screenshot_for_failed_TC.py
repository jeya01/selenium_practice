from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.save_screenshot("C:\\Users\\jeyalakshmi\\PycharmProjects\\pavan_selenium_2022\\nop-screenshot.png")
driver.save_screenshot(os.getcwd()+"\\nop-screenshot.png")

driver.close()
