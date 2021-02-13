
from selenium import webdriver
class MainPage:
    button_click_xpath="//header/div[1]/div[1]/nav[1]/nav[1]/ol[1]/li[7]/ol[1]/li[2]/a[1]"
    link_createaccount_xpath="//button[@id='form-button-create']"
    first_textbox_xpath="//input[@id='form-input-first_name']"
    last_textbox_xpath="//input[@id='form-input-last_name']"
    email_textbox_xpath="//input[@id='form-input-email']"
    password_text_xpath="//input[@id='form-input-password']"
    click_box_xpath="//body/div[1]/main[1]/div[1]/div[2]/form[1]/div[5]/fieldset[1]/div[1]/div[1]/label[1]"
    click_createAccount_xpath="//button[@id='form-submit-continue']"


    def __init__(self,driver):
        self.driver=driver

    def clickMain(self):
        self.driver.find_element_by_xpath(self.button_click_xpath).click()
    def createAccount(self):
        self.driver.find_element_by_xpath(self.link_createaccount_xpath).click()
    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.first_textbox_xpath).send_keys(firstname)
    def setLastname(self,lastname):
        self.driver.find_element_by_xpath(self.last_textbox_xpath).send_keys(lastname)
    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)
    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.password_text_xpath).send_keys(password)
    def clickbox(self):
        self.driver.find_element_by_xpath(self.click_box_xpath).click()
    def createNewaccount(self):
        self.driver.find_element_by_xpath(self.click_createAccount_xpath).click()



