from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

class ElementState():

    def isEnabled(self):
        baseUrl = "http://www.google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element(By.XPATH, "//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
        e1State = e1.is_enabled() # True for enabled and False for disabled
        print("E1 is Enabled? -> " + str(e1State))


        e1.send_keys("letskodeit")
        time.sleep(3)


e = ElementState()
e.isEnabled()