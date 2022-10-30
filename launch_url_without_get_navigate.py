from selenium import webdriver


driver = webdriver.Chrome()

driver.execute_script("window.location = 'https://www.google.com/'")

driver.close()