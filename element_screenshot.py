import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#logo = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[1]/img")
#logo.screenshot("logo.png")
time.sleep(5)
# username = driver.find_element(By.XPATH,"//input[@name='username']")
# print(username.location)  # prints the location of the element
# print(username.size) # prints the height and width of the element
# username.screenshot_as_png # returns current element in binary format
partt = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]")
partt.screenshot("part.png")
driver.close()