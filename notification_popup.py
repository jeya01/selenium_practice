

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver = webdriver.Chrome()
url = "https://www.gps-coordinates.net/my-location"
driver.get(url)
driver.maximize_window()