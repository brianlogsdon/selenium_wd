from selenium import webdriver
import os

class RunFFTests():

    def testMethod(self):
        # Instantiate browser command
        driver = webdriver.Firefox()
        # Open the provided URLs
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()