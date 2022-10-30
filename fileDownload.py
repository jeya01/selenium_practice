import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

location = os.getcwd()
print(location)


def chrome_setup():
    from selenium.webdriver.chrome.service import Service

    s = Service("D:\Selenium Drivers\chromedriver.exe")

    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(service=s,options=ops)
    return driver

def edge_setup():
    from selenium.webdriver.edge.service import Service

    s = Service("D:\Selenium Drivers\msedgedriver.exe")
    preferences = {"download.default_directory", location}

    ops = webdriver.EdgeOptions()

    driver = webdriver.Edge(service=s,options=ops)

    ops.add_experimental_option("prefs", preferences)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    s = Service("D:\Selenium Drivers\geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","image/png") #application/png - application type
    # mime type list https://www.sitepoint.com/mime-types-complete-list/
    #ops.set_preference("browser.download.manager.showWhenStarting",False) no longer needed. firefox stopped showing the pop up
    ops.set_preference("browser.download.folderList",2) # 0 - desktop 1 - default download location 2 - specified location
    ops.set_preference("browser.download.dir",location)
    driver= webdriver.Firefox(service=s,options=ops)
    return driver



#driver = chrome_setup()
#driver = edge_setup()
driver = firefox_setup()
driver.get("https://www.leafground.com/file.xhtml")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[normalize-space()='Download']").click()
time.sleep(5)



driver.close()