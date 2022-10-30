import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()
time.sleep(5)
print(driver.switch_to.active_element.text) #This returns the text value of active elemeent
driver.close()