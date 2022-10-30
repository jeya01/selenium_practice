from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''Implicit wait'''
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
#
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='W0wltc']/div").click()
# search = driver.find_element(By.NAME,"q")
# search.send_keys("selenium")
# search.submit()
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
# driver.close()

'''Explicit wait'''
driver = webdriver.Chrome()

exp_wait = WebDriverWait(driver,10) #explicit wait declaration
#exp_wait = WebDriverWait(driver,timeout= 10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,Exception]) #Fluent wait

driver.get("https://www.google.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='W0wltc']/div").click()
search = driver.find_element(By.NAME,"q")
search.send_keys("selenium")
search.submit()
search_text = exp_wait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))


driver.close()