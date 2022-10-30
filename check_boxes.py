import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()


#driver.find_element(By.CSS_SELECTOR,"input#monday").click()
chk_boxes = driver.find_elements(By.CSS_SELECTOR,"input.form-check-input[type='checkbox']")
print(len(chk_boxes))

#approach 1
# for i in range(0,len(chk_boxes)):
#     chk_boxes[i].click()

#apprach 2
# for chk in chk_boxes:
#     chk.click()

#select check box based on condition
# for chk in chk_boxes:
#     print(chk.get_attribute('id'))
#     weekname = chk.get_attribute('id')
#     if weekname == 'monday':
#         chk.click()

#selecting last two check boxes
# for i in range(len(chk_boxes)-2,len(chk_boxes)):
#     chk_boxes[i].click()

#selecting first two check boxes
# for i in range(len(chk_boxes)):
#     if i < 2:
#         chk_boxes[i].click()

btn = driver.find_element(By.CSS_SELECTOR,"button[name='submit']")
print(f'Location:{btn.location},Size:{btn.size}')

for chk in chk_boxes:
    if chk.is_selected():
        chk.click()

time.sleep(3)
for chk in chk_boxes:
    chk.click()




driver.close()