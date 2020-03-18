from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKey ():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()



        email_field = driver.find_element(By.ID, "user_email")
        email_field.send_keys("test")

        password_field = driver.find_element(By.ID, "user_password")
        password_field.send_keys("test")

        time.sleep(3)
        email_field.clear()
        time.sleep(3)
        email_field.send_keys("test")




cc=ClickAndSendKey()
cc.test()