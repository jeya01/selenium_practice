import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

slider_min = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
slider_max = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")
print(slider_min.location)  # {'x': 59, 'y': 251} '''as it is horizontal we are only changing x axis.'''
print(slider_max.location)  # {'x': 613, 'y': 251}''' if it is vertical then y aixs should be changed'''
act = ActionChains(driver)


act.drag_and_drop_by_offset(slider_min, 100, 0).perform() # increse for right side
act.drag_and_drop_by_offset(slider_max, -50, 0).perform() # decrease for left side

print(slider_min.location) # {'x': 159, 'y': 251}
print(slider_max.location) # {'x': 563, 'y': 251}

time.sleep(3)
driver.close()
