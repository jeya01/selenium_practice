import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
driver.maximize_window()

driver.switch_to.frame("iframeResult")
act = ActionChains(driver)
double_click = driver.find_element(By.XPATH,"/html/body/p[1]")
act.double_click(double_click).perform()

time.sleep(3)
driver.close()