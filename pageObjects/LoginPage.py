# from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_Page:
    Textbox_username_id = "email"
    Textbox_password_id= "login-password"
    button_login_id = "login"
    link_logout_linktext = "Logout"


    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        self.driver.find_element(By.ID,self.Textbox_username_id).clear()
        self.driver.find_element(By.ID,self.Textbox_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.Textbox_password_id).clear()
        self.driver.find_element(By.ID,self.Textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID,self.button_login_id).click()





