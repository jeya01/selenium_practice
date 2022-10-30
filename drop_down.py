from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()


dropdown = driver.find_element(By.CSS_SELECTOR,"select#input-country")
dropdown_country = Select(dropdown)

#select option from dropdown
#dropdown_country.select_by_visible_text('India')

#dropdown_country.select_by_value('19') #value is available in the html while inspect
dropdown_country.select_by_index(12)

#printingg all available from the dropdown
available_opions = dropdown_country.options
# for option in available_opions:
#     print(option.text)


'''selecting the option from dropdowm without using built in function'''
for option in available_opions:
    if option.text == 'India':
        option.click()

'''select using send keys'''
#dropdown.send_keys("India")
