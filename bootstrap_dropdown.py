from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
drop_down = driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
countries_list = driver.find_elements(By.XPATH,"//ul[@class='select2-results__options']/li")

for country in countries_list:
    if country.text == 'India':
        country.click()
        break


driver.close()