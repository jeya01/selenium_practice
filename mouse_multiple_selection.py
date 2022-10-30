import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/selectable/")
driver.maximize_window()
driver.switch_to.frame(0) #because there is only one frame available
item1 = driver.find_element(By.XPATH,"//li[text()='Item 1']")
item2 = driver.find_element(By.XPATH,"//li[text()='Item 2']")
act = ActionChains(driver)
act.key_down(Keys.CONTROL).move_to_element(item1).click().move_to_element(item2).click().key_up(Keys.CONTROL).perform()
time.sleep(5)

driver.close()