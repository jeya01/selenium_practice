from selenium import webdriver

def headless_chrome():

    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(options=ops) # i didnt pass service obj as the path specified in enviroment variable
    return driver


def headless_edge():

    ops = webdriver.EdgeOptions()
    ops.headless = True
    driver = webdriver.Edge(options=ops) # i didnt pass service obj as the path specified in enviroment variable
    return driver


def headless_firefox():

    ops = webdriver.FirefoxOptions()
    ops.headless = True
    driver = webdriver.Firefox(options=ops) # i didnt pass service obj as the path specified in enviroment variable
    return driver


#driver = headless_edge()
driver = headless_firefox()
driver.get("https://demo.nopcommerce.com/")
print("Title of the page:",driver.title)
print("URL of the page:",driver.current_url)
driver.close()