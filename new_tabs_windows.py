import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")


'''To open a link in another tab'''
reglink = Keys.CONTROL+Keys.ENTER
#driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

#driver.switch_to.new_window("tab") # one of the new feature in selenium 4
'''to open in a new window'''
driver.switch_to.new_window("window") # one of the new feature in selenium 4
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()

'''switch to window takes window id as argument new window takes window as argument to open another window'''