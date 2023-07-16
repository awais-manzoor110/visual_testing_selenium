from selenium.webdriver.common.by import By
from utilities.baseclass import BaseClass
from utilities.eye_manager import Eyes_Manager


class Test_One(BaseClass):

    def test_exploring(self, eyes):
        eye = Eyes_Manager()
    #     # page = SearchPage(self.driver)
    #     # page.filter_books('james')
    #     # validate_window(self.driver, eyes)
        element = self.driver.find_element(By.XPATH, "//div[@class='OrgAvatarLink-logo']")
        eye.validate_element(self.driver, eyes, element, tag="first test")

    def test_two(self, eyes):
        eye = Eyes_Manager()
        eye.validate_window(self.driver, eyes, tag="second test")



