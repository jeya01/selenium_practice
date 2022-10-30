import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd()
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service("D:\Selenium Drivers\chromedriver.exe")

preferences = {"download.default_directory": location,"plugins.always_open_pdf_externally":True}
ops = webdriver.ChromeOptions()
ops.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(service=s,options=ops)


driver.get("")
driver.maximize_window()

time.sleep(3)

