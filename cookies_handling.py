'''Take the application
check the app creating cookies or not
check what kind of cookies
take cookie attributes and values
control cookies through automation
we can also create our won cookie
delete the cookies
cookies are dynamic
'''

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
'''capture all the cookies'''
all_cookie = driver.get_cookies()
print(all_cookie) # returns a list of dictionary collection
print(len(all_cookie))
for info in all_cookie:
    # print(info.keys()) #print the keys from the dictionary collection
    # print(info.values()) # print the values of the keys
    # print(info['name']) # or  print(info.get('name'))
    print(info['name'] ,":" , info['value'])


'''adding own cookie'''
driver.add_cookie({"name" : "mycookie" , "value" : "11345"})
new_cookie = driver.get_cookies()
print("after adding a new cookie",len(new_cookie))
print(new_cookie)

driver.delete_cookie("mycookie")
new_cookie = driver.get_cookies()
print("after deleting:",len(new_cookie))

# delete all the cookies

driver.delete_all_cookies()
new_cookie = driver.get_cookies()
print("Delete all the cookies:",len(new_cookie))

# adding a new cookie after deleting all the cookies
driver.add_cookie({"name" : "mycookie" , "value" : "11345"})
new_cookie = driver.get_cookies()
print("after adding a new cookie",len(new_cookie))
print(new_cookie)



driver.close()