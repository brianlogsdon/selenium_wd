from selenium import webdriver

class FindByIdName ():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByID = driver.find_element_by_id("name")

        if elementByID is not None:
            print("We found an element by Id")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print("We found an element by name")


ff = FindByIdName()
ff.test()