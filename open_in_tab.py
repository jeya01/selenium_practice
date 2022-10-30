import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.execute_script("window.open('');") # opens new tab
driver.switch_to.window(driver.window_handles[1]) # switch to the newly opened tab
driver.get("https://www.google.com") # opens the url
driver.switch_to.window(driver.window_handles[0]) # comes back to the old tab
'''second method
driver.switch_to.new_window('tab')

'''
driver.close() #closes the current window
