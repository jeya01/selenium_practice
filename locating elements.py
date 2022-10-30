import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

'''Locating thee elements in a DOM'''

url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()
'''locating elements'''
#driver.find_element(By.NAME,"specify the name of the element")
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Mobile Phones")

driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
#driver.set_page_load_timeout(3)
# driver.find_element(By.LINK_TEXT,"Mobile phone").click()
#
# driver.find_element(By.PARTIAL_LINK_TEXT,"aircraft").click()
time.sleep(5)

links = driver.find_elements(By.XPATH,"//*[@id='wikipedia-search-result-link']")
print(len(links))
for link in links:
    print(link)

driver.close()

"""flipkart
search iphone 13 - find all the hyperlink
find the price of an phone which is greater than 70000"""