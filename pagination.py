import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://datatables.net/examples/advanced_init/dt_events.html")
driver.maximize_window()

pagination = driver.find_elements(By.XPATH,"//*[@id='example_paginate']//a")
print(len(pagination))
#button_six = driver.find_element(By.XPATH,"//*[@id='example_paginate']/span/a[6]").click()
count = 0
while True:
    next_button = driver.find_element(By.XPATH,"//a[@id='example_next' and text()='Next']")
    next_button_attribute = next_button.get_attribute('class')
    print(next_button_attribute)
    if not next_button_attribute.__contains__("disabled"):
        next_button.click()
    else:
        break





driver.close()
