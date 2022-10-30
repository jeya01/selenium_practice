

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

'''Method 1'''
'''Tag and Id combination
name of the tag#id or just #id'''
#email = driver.find_element(By.CSS_SELECTOR,"input#email")

'''Method 2
    Tag and class combination
    tag.valueoftheclass'''

'''input.inputtext _55r1 _6luy _9npi here there is a space before _, 
so it throws no such element exception remove the text after the space'''

'''what if different element has same class name'''
#pwd = driver.find_element(By.CSS_SELECTOR,"input.inputtext")


'''Method 3
    Tag and attribute and its value combination
    tagname[attribute=value]
    eg:input[data-testid='royal_login'] or [data-testid='royal_login']'''

#id1 = driver.find_element(By.CSS_SELECTOR,"input[data-testid='royal_login']")


'''Method 4
    Tag, class and attribute combination
    tagname.value of class[attribute=value]
    This can be used when the different element shares the same class name. The webdriver locate by default the first element
    To locate the second or further elements that shares the same class name this method should be used'''
driver.find_element(By.CSS_SELECTOR,"input.inputtext[type='password']")

driver.close()