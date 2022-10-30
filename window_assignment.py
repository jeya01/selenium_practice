import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.set_page_load_timeout(10)

driver.maximize_window()
'''locating elements'''
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("google")
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
time.sleep(5)
links = driver.find_elements(By.XPATH,"//a[contains(text(),'Google')]")
print(len(links))
for link in links:
    link.click()


open_windows = driver.window_handles
for win_id in open_windows:
    driver.switch_to.window(win_id)
    print(driver.title)
