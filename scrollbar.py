import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

''' option 1 
scroll down based on pixel value
'''
# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Scrolled until:", value)

''' option 2
scroll down based on element is visible
'''
singapore = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[63]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",singapore)
time.sleep(5)

'''option 3
scroll until end of the page'''

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll to end of the page
# time.sleep(5)
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)") #scroll up to the beginning of the page
# time.sleep(3)


'''option 4 using ActionChains and Keys'''
act = ActionChains(driver)
act.click().perform()
act.key_down(Keys.DOWN).perform()
act.key_up(Keys.DOWN).perform()
time.sleep(5)
act.key_down(Keys.UP).perform()
act.key_up(Keys.UP).perform()
time.sleep(5)
driver.close()