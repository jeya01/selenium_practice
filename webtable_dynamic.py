import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()


username = driver.find_element(By.XPATH,"//*[@name='username']")
username.send_keys("Admin")
password = driver.find_element(By.XPATH,"//*[@name='password']")
password.send_keys("admin123")
submit = driver.find_element(By.XPATH,"//*[@type='submit']")
submit.click()
driver.find_element(By.XPATH,"//span[text()='Admin']").click()
