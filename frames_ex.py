'''Frames/iFrames'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/package-summary.html")
driver.maximize_window()



'''
driver.switch_to.frame(name of the frame)
driver.switch_to.frame(id of the frame)
driver.switch_to.frame(web element)
driver.switch_to.frame(index) - use when there are not many frames
driver.switch_to_frame() - selenium 3 '''
# Frame 1
driver.switch_to.frame("packageListFrame") #switch_to is a property of a driver, it is like a instance variable
driver.find_element(By.XPATH,"/html/body/main/ul/li[1]/a").click()
driver.switch_to.default_content()

#Frame 2
driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//span[text()='WebDriver']").click()
driver.switch_to.default_content()

#Frame 3
driver.switch_to.frame("classFrame")
driver.find_element(By.LINK_TEXT,"HELP").click()



driver.close()