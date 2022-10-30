import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()
search_box= driver.find_element(By.NAME,"q")
search_box.send_keys("selenium",Keys.ENTER) #method 3
#search_box.send_keys("selenium \n",) #method 4 using new line character
'''Ways to press enter key to perform Google search method 1 '''
# act = ActionChains(driver)
# act.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

'''Ways to press enter key to perform Google search method 2 '''

#search_box.submit()
#time.sleep(10)
# 1.//*[contains(@class,'pcTkSc')]"
# 2.//ul[@role='listbox']//li/descendant::div[@class='pcTkSc']//descendant::b"
# 3. //ul[@class='G43f7e']/li



# to print all the links from the google search result
# search_result = driver.find_elements(By.XPATH,"//a")
# print(len(search_result))
# for result in search_result:
#      print(result.get_attribute("href"))


# to print the main links from the google search result
# main_result = driver.find_elements(By.XPATH,"//*[@id='search']//following::h3//following::div[1]/cite[@role='text']")
# print(len(main_result))
# for result in main_result:
#     print(result.text)


'''Click a Google suggestion for the given search Term'''
