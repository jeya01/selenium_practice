import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"OrangeHRM, Inc").click()
current_id = driver.current_window_handle # return id of single window
multiple_window= driver.window_handles   # return ids of all the opened window
#driver.switch_to.window() #browser window id
# parent_window = multiple_window[0]
# child_window =  multiple_window[1]
# print("Title of the parent Window:",driver.title)
# driver.switch_to.window(child_window)
# print("The title of the child window",driver.title)
# time.sleep(3)
# driver.switch_to.window(parent_window)
# print("Title of the parent Window:",driver.title)

for win_id in multiple_window:
    driver.switch_to.window(win_id)
    print(driver.title)



