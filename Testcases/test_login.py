# import pytest
# from selenium import webdriver
from pageObjects.LoginPage import Login_Page
import time
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen

class Test_001_login:
    base_url =Readconfig.getApplicati0nURL()
    username = Readconfig.get_username()
    password = Readconfig.get_password()
    logger = LogGen.loggen()


    def test_homepage_title(self,setup):
        self.logger.info("************* Test_001_login ************ ")
        self.logger.info("************* verifying started **************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        act_title = self.driver.title
        print(""+str(act_title))
        self.driver.close()
        if act_title =="Login":
            assert True
            time.sleep(6)
            self.logger.info("************* Home Page Title test is passed **************")
        else:
            self.driver.save_screenshot(".\\Screen_shots\\"+"test_homepage_title.png")
            self.logger.error("************* Home Page Title test is failed **************")
            time.sleep(7)
            assert False

    def test_login(self,setup):
        self.logger.info("************ Login Page Title test is started **************")
        self.logger.info("************  Verifying started **************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.lp =Login_Page(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(8)
        act_title = self.driver.title
        self.driver.quit()


        if act_title == "My Courses":
            print(""+str(act_title))
            assert True
            time.sleep(6)
            self.logger.info("************ Login Page Title test is passed **************")


        else:
            self.driver.save_screenshot(".\\Screen_shots\\" + "test_login.png")
            time.sleep(6)
            self.logger.error("*********** Login Page Title test is failed **************")
            assert  False







