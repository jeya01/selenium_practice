from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()

driver.maximize_window()
deutsch = driver.find_element(By.XPATH,"//a[contains(text(),'English')]")
before_hover = deutsch.value_of_css_property("text-decoration")
print(before_hover)
act = ActionChains(driver)
act.move_to_element(deutsch).perform()
after_hover = deutsch.value_of_css_property("text-decoration")
print(after_hover)
driver.close()
