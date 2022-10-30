import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()
search_box= driver.find_element(By.NAME,"q")
search_box.click()
search_box.send_keys("selenium")
time.sleep(5)
# 1.//*[contains(@class,'pcTkSc')]"
# 2.//ul[@role='listbox']//li/descendant::div[@class='pcTkSc']//descendant::b"
# 3. //ul[@class='G43f7e']/li
search_list = driver.find_elements(By.XPATH,"//ul[@class='G43f7e']/li")
print(len(search_list))

for search in search_list:
    print(search.text)



driver.close()