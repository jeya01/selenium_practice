import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

# ops = webdriver.ChromeOptions()
# ops.add_argument("incognito")
# ops.add_argument("start-maximized")
#
# driver = webdriver.Chrome(options=ops)
driver  = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()


driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()

driver.get(driver.current_url) # refreshing page udingg current_url
time.sleep(3)

# gmail = driver.find_element(By.XPATH, "//*[@id='gb']/div/div[1]/div/div[1]/a")
# print(gmail.get_attribute("innerHTML"))  # innerHTML retrives the text betweem the open and close tags
driver.close()