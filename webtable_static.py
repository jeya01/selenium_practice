import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#1.Count no of rows and columns in a table
no_of_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
row_len = len(no_of_rows)
print("No of rows:",row_len) #includes the header as well

no_of_cols = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[1]/th")
col_len = len(no_of_cols)
print("No of columns",col_len)


#2. Read specific data from the table
output = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(output)

#3.Read all the columns and rows data
print("Read all the datas from the table ............")
for row in range(2,row_len+1):
    for col in range(1,col_len+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(data, end = "     ")
    print()

#4.Read the table data based on the condition(list the book names whose author is Mukesh)
print("Read the table data based on the condition(list the book names whose author is Mukesh)")
for row in range(2,row_len+1):
    author = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[2]").text
    if author == 'Mukesh':
        name_of_book = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[1]")
        price = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td[4]")
        print(f"name of the book:{name_of_book.text}, and the price is: {price.text} for the author{author}",end="\n")





driver.close()