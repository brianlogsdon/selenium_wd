from selenium import webdriver
import os
class ChromeDriverMac():
    def test(self):
        #Instantiate browser command
        driver = webdriver.Chrome()
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

cc = ChromeDriverMac()
cc.test()