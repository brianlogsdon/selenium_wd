from selenium import webdriver

class SafariDriverMac():
    def test(self):
        driver = webdriver.Safari()

        driver.get("http://www.letskodeit.com")

sf = SafariDriverMac()
sf.test()

