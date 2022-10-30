import time

from selenium import webdriver
from selenium.webdriver.common.by import By
""""When the user is unable to locate the driver location WebDriverManager is used to download and install the browser"""
'''chrome driver and driver manager'''
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

'''Firefox driver and driver manager'''
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.firefox import GeckoDriverManager



url = "https://www.google.com"

def launchBrowser(browser):

    if browser == "chrome":
        ch_driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
        ch_driver.get(url)
       # ch_driver.find_element(By.NAME,"q").send_keys("google")

    else:
        ff_driver = webdriver.Firefox(service=firefoxService(GeckoDriverManager().install()))
        ff_driver.get(url)

      #  ff_driver.find_element(By.NAME,"q").send_keys("google")



launchBrowser("chrome")
