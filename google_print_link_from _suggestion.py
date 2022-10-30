import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()
search_box= driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
search_box.click()
#time.sleep(10)
# 1.//*[contains(@class,'pcTkSc')]"
# 2.//ul[@role='listbox']//li/descendant::div[@class='pcTkSc']//descendant::b"
# 3. //ul[@class='G43f7e']/li
search_list = driver.find_elements(By.XPATH,"//ul[@class='G43f7e']/li")
print(len(search_list))

''' One click a search term based on position and the next one click a search term with a certain keyword.'''
# position = 0
# for search in search_list:
#     print(search.text)
#     position += 1
#     if position == 3:
#         search.click()
#         break # this will break the loop after clicking the element otherwise it will throw nosuchwindow exception
#


#based on the search Term


for search in search_list:
    print(search.text)
    #if search.text.__contains__("ide"):
    if "ide" in search.text:
        search.click()
        break




