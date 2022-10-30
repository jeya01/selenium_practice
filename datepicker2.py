import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Buy Ticket']").click()
dob = driver.find_element(By.XPATH,"//*[@id='dob']")
dob.click()
month = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_visible_text("Apr")
year = Select(driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
year.select_by_visible_text("2008")
alldates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in alldates:
    if date.text=="18":
        date.click()
        break


time.sleep(5)

driver.close()