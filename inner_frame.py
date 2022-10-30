import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

'''here we use frame as a webelement'''
outer_frame = driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(outer_frame)
inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("hello")
'''As it is inner frame we dont need to go to the driver.switch_to.default_content() . driver.switch_to.default_content() 
this is used when the frames are different'''
driver.switch_to.parent_frame() # this helps to switch to parent frame when there are any elements available in parent frame

time.sleep(3)
driver.close()
