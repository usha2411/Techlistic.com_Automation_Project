

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.login_form import Login_Form

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    login_form = Login_Form(driver)
    login_form.open_page("https://www.techlistic.com/p/selenium-practice-form.html")

    login_form.enter_firstname("Usha")
    login_form.enter_lastname("Nazare")
    login_form.enter_sex()
    login_form.enter_experience()
    login_form.enter_date("20-5-2025")
    login_form.enter_profession()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "profession-1"))).click()
    time.sleep(2)
    login_form.enter_tool()
    time.sleep(2)
    login_form.enter_drp1()
    login_form.enter_drp2()
    login_form.enter_image("D:/OneDrive/Pictures/Screenshots/Screenshot 2025-07-25 110819.png")
    time.sleep(1)
    login_form.enter_submit()
    time.sleep(3)
    driver.save_screenshot(".\\screenshots\\successful_login.png")
