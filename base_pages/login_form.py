import time

from selenium.webdriver.common.by import By


class Login_Form():
    def __init__(self,driver):
        self.driver=driver
        self.firstname=(By.NAME,"firstname")
        self.lastname=(By.NAME,"lastname")
        self.sex=(By.XPATH,"//input[@id='sex-1']")
        self.experience=(By.XPATH,"//*[@id='exp-2']")
        self.date=(By.ID,"datepicker")
        self.profession=(By.XPATH,"//input[@id='profession-1']")
        self.tool=(By.ID,"tool-2")
        self.drp1=(By.XPATH,"//option[normalize-space()='Africa']")
        self.drp2=(By.XPATH,"//option[normalize-space()='Wait Commands']")
        self.image=(By.XPATH,"//input[@id='photo']")
        self.submit=(By.ID,"submit")


    def open_page(self,url):
        self.driver.get(url)

    def enter_firstname(self, firstname):
        self.driver.find_element(*self.firstname).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*self.lastname).send_keys(lastname)

    def enter_sex(self):
        self.driver.find_element(*self.sex).click()

    def enter_experience(self):
        self.driver.find_element(*self.experience).click()

    def enter_date(self,date):
        self.driver.find_element(*self.date).send_keys(date)

    def enter_profession(self):
        self.driver.find_element(*self.profession).click()

    def enter_tool(self):
        self.driver.find_element(*self.tool).click()

    def enter_drp1(self):
        self.driver.find_element(*self.drp1).click()

    def enter_drp2(self):
        self.driver.find_element(*self.drp2).click()

    def enter_image(self, image_path):
        self.driver.find_element(*self.image).send_keys(image_path)

    def enter_submit(self):
        self.driver.find_element(*self.submit).click()

