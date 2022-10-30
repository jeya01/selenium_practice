import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

'''
ctrl + A
ctrl + C
tab
ctrl + v
'''
driver.get("https://text-compare.com/")
driver.maximize_window()

input_text1 = driver.find_element(By.ID,"inputText1")
input_text1.send_keys("Welcome to selenium keyboard control module")
input_text2 = driver.find_element(By.ID,"inputText2")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() # action.press control + A. release control
# and perform the action

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()