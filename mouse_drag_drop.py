from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)
rome = driver.find_element(By.ID,"box6") #source element
italy = driver.find_element(By.ID,"box106") #target element
act.drag_and_drop(rome,italy).perform()
