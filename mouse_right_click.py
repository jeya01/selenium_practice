from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

right_click = driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")

act = ActionChains(driver)

act.context_click(right_click).perform()