'''alert is not an webelement'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

'''use this for alert window'''
#driver.get("https://the-internet.herokuapp.com/javascript_alerts")

'''alert window with input box, OK and Cancel button'''
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//button[contains(text(),'JS Prompt')]").click()
# alert_box = driver.switch_to.alert
# print(alert_box.text) #Prints alert bo text
#
# alert_box.send_keys("welcome")
# #alert_box.accept() # close alert box by clicking OK button
# alert_box.dismiss() # close alert box by clicking cancel button


'''alert window with OK button'''
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
# time.sleep(3)
# alert_box = driver.switch_to.alert
# alert_box.accept()

'''authentication pop up'''

'''injecting the user name and password'''
'''send keys wont work in authentication pop up because it has two input boxes
https://admin:admin@the-internet.herokuapp.com/basic_auth
here the 1st admin is username and 2nd admin is a password 
'''
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)
driver.close()

