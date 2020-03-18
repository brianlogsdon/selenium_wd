from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Find departing field
        departingField = driver.find_element_by_id("flight-departing-hp-flight")
        # Click departing field
        departingField.click()
        # Find the date to be selected

        # Updated new xpath
        dateToSelect = driver.find_element(By.XPATH,
                                           "//*[@id='flight-departing-wrapper-hp-flight']//td[2]/button[text ()= ' 30']")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Click departing field
        driver.find_element_by_id("flight-departing-hp-flight").click()

        # Updated new xpath
        calMonth = driver.find_element(By.XPATH, "//div[@class='datepicker-cal-month'][position()=1]")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

        time.sleep(2)

        for date in allValidDates:
            
            if date.text == " 30":
                date.click()
                break


ff = CalendarSelection()
ff.test2()

