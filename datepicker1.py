from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("10/20/2022")
day = "18"
month = "June"
year =  "2018"



driver.find_element(By.XPATH, "//*[@id='datepicker']").click()
while True:
    mon = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text
    yr = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text
    if month == mon and year == yr:
        break
    else:
        #driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click() #clicking next arrow
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() # clicking previous arrow


dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for ele in dates:
    if ele.text == day:
        ele.click()
        break