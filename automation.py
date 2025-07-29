import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(2)

driver.find_element(By.NAME,"firstname").send_keys("Usha")
driver.find_element(By.NAME,"lastname").send_keys("Nazare")
driver.find_element(By.XPATH,"//input[@id='sex-1']").click()
driver.find_element(By.XPATH,"//*[@id='exp-2']").click()
driver.find_element(By.ID,"datepicker").click()
driver.find_element(By.ID,"datepicker").send_keys("20-05-2025")
driver.find_element(By.ID,"profession-1").click()
driver.find_element(By.XPATH,"//input[@id='tool-2']").click()
driver.find_element(By.XPATH,"//input[@id='tool-0']").click()

# #by using select class
drp1=driver.find_element(By.XPATH,"//select[@id='continents']")
obj=Select(drp1)
obj.select_by_visible_text("Australia")
time.sleep(1)
#
# # # drp1=driver.find_element(By.XPATH,"//select[@id='continents']")
# # # drp1.find_element(By.XPATH,"//option[normalize-space()='Africa']").click()
# # # time.sleep(2)
#
drp2=driver.find_element(By.ID,"selenium_commands")
opt=Select(drp2)
opt.select_by_visible_text("WebElement Commands")

image=driver.find_element(By.XPATH,"//input[@id='photo']")
image.send_keys("D:/OneDrive/Pictures/Screenshots/Screenshot 2025-07-25 110819.png")
time.sleep(2)

driver.find_element(By.ID,"submit").click()
time.sleep(2)