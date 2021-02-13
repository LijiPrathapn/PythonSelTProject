import pytest
from selenium import webdriver
from PageObjects.MainPage import MainPage

class Test_01_Main:
    baseURL="https://www.tesla.com/"
    firstname="Liji"
    lastname="Prathapan"
    email="liji.prathapan@gmail.com"
    password="Belkin09!"

    # def test_homePageTitle(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     if act_title=="Electric Cars, Solar &amp; Clean Energy | Tesla":
    #         assert True
    #     else:
    #         self.driver.save_screenshot("C:\\Users\\lijin\\PycharmProjects\\TeslaProject\\Screenshots"+"test_homePageTitle.png")
    #         self.driver.close()
    #         assert False
    def test_main(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.mp = MainPage(self.driver)
        self.mp.clickMain()
        self.mp.createAccount()
        self.mp.setFirstname(self.firstname)
        self.mp.setLastname(self.lastname)
        self.mp.setEmail(self.email)
        self.mp.setPassword(self.password)
        self.mp.clickbox()
    #     self.mp.createNewaccount()
    # print("Test Completed")




