'''Broken Links'''
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

count = 0
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
for link in links:
    url = link.get_attribute('href')

    try:
        res = requests.head(url)

    except:
        None

    if res.status_code >=400:
        print(url, "  this is a broken link")
        count += 1
    else:
        print(url, "  This is a valid link")


print("Total no broken of links", count)

driver.close()