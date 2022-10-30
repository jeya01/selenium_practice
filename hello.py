from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(10)



# driver.implicitly_wait(5) # Implicit wait

#Explicit wait


url = driver.get("https://en.wikipedia.org/wiki/India")
driver.set_page_load_timeout(10)

driver.maximize_window()
a = driver.find_element(By.CSS_SELECTOR,"")

# get element  after explicitly waiting for 10 seconds
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "//*[@id='layout-config-button']/i")))
# # click the element
# element.click()
# time.sleep(3)

# driver.fullscreen_window() # window will full screen

driver.close()