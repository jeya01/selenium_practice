'''Mouse actions
1.mouse hover move_to_element(element)
2.Right click context_click(element)
3.Double click double_click(element)
4.Drag and drop
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.leafground.com/dashboard.xhtml")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//*[@id='menuform']/ul[1]/li[3]")
wait_link = driver.find_element(By.XPATH,"//*[@id='menuform:m_wait']/a")
act = ActionChains(driver)
act.move_to_element(element).click().move_to_element(wait_link).click().perform() #here we have to click first to start the mousehover

