from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Login():
    def login(self):
        driver = webdriver.Chrome()
        base_url = "https://www.letskodeit.com/"
        driver.get(base_url)
        driver.maximize_window()
        driver.implicitly_wait(6)


        driver.find_element(By.XPATH,"//a[text()='Sign In']").click()
        driver.find_element(By.ID,"email").send_keys("test@email.com")
        driver.find_element(By.ID,"login-password").send_keys("abcabc")
        driver.find_element(By.XPATH,"//*[@id='login']").click()
        time.sleep(7)
        my_title = driver.title
        print(""+str(my_title))
        # if my_title =="My Courses":
        #         assert True
        # else:
        #         assert False


lp = Login()
lp.login()



